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
    success_url = reverse_lazy('service_list')
    print('1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm(self.request.POST or None)
        context['phone_form'] = PhoneNumberForm(self.request.POST or None)
        context['address_form'] = AddressForm(self.request.POST or None)
        print('2')
        return context

    def form_valid(self, form):
        user_form = UserForm(self.request.POST)
        phone_form = PhoneNumberForm(self.request.POST)
        address_form = AddressForm(self.request.POST)
        print('3')


        if user_form.is_valid() and phone_form.is_valid() and address_form.is_valid():
            # Aqui, adicionar username se necessário
            if 'username' not in user_form.cleaned_data:
                user_form.cleaned_data['username'] = user_form.cleaned_data['email']  # Exemplo, pode ser ajustado

            if User.objects.filter(email=user_form.cleaned_data['email']).exists():
                user_form.add_error('email', 'Este e-mail já está em uso.')
                return self.form_invalid(form)
            
            try:
                with transaction.atomic():
                    print('4')
                    print("Dados do usuário:", user_form.cleaned_data)
                    print("Dados do telefone:", phone_form.cleaned_data)
                    print("Dados do endereço:", address_form.cleaned_data)

                    user = user_form.save()

                    # Associar o telefone e o endereço ao usuário
                    phone = phone_form.save(commit=False)
                    phone.user = user
                    phone.save()

                    address = address_form.save(commit=False)
                    address.user = user
                    address.save()

                return super().form_valid(form)
            except IntegrityError as e:
                print('5 - IntegrityError:', str(e))  # Exibe o erro real no console
                user_form.add_error(None, f'Erro ao salvar os dados: {str(e)}')
                user_form.add_error(None, 'Ocorreu um erro ao tentar salvar os dados.')
                return self.form_invalid(form)
        print('6')
        return self.form_invalid(form)
