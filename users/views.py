from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db import IntegrityError, transaction
from .models import User, PhoneNumber, Address
from .forms import UserForm, PhoneNumberForm, AddressForm

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm(self.request.POST or None)
        context['phone_form'] = PhoneNumberForm(self.request.POST or None)
        context['address_form'] = AddressForm(self.request.POST or None)
        return context

    def form_valid(self, form):
        # Criação dos formulários
        user_form = UserForm(self.request.POST)
        phone_form = PhoneNumberForm(self.request.POST)
        address_form = AddressForm(self.request.POST)

        # Verificar se todos os formulários são válidos
        if user_form.is_valid() and phone_form.is_valid() and address_form.is_valid():
            # Verificar se o e-mail já existe no banco de dados
            if User.objects.filter(email=user_form.cleaned_data['email']).exists():
                user_form.add_error('email', 'Este e-mail já está em uso.')
                return self.form_invalid(form)

            try:
                # Usando uma transação atômica para garantir que todas as operações sejam realizadas com sucesso
                with transaction.atomic():
                    # Salvar o usuário
                    user = user_form.save()

                    # Associar o telefone e o endereço ao usuário
                    phone = phone_form.save(commit=False)
                    phone.user = user
                    phone.save()

                    address = address_form.save(commit=False)
                    address.user = user
                    address.save()

                # Se tudo correr bem, redireciona após o sucesso
                return super().form_valid(form)
            except IntegrityError:
                # Se ocorrer algum erro durante a transação, podemos tratar aqui
                user_form.add_error(None, 'Ocorreu um erro ao tentar salvar os dados.')
                return self.form_invalid(form)
        
        # Se qualquer formulário não for válido, retorna erro
        return self.form_invalid(form)