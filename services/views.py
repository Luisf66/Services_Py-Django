from services.models import Service
from services.forms import ServiceModelForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
# Create your views here.

class NewServiceCreateView(CreateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'new_service.html'

    def get_success_url(self):
        return reverse_lazy('services')

class ServiceListView(ListView):
    model = Service
    template_name = 'services_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        query = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            query = query.filter(name__icontains=search)
        return query

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'service_update.html'

    def get_success_url(self):
        return reverse_lazy('service_detail', kwargs={'pk': self.object.pk})

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_delete.html'
    success_url = '/services/'