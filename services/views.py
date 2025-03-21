from services.models import Service
from services.forms import ServiceModelForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
# Create your views here.

class NewServiceCreateView(CreateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'new_service.html'
    success_url = '/services/'

class ServiceListView(ListView):
    model = Service
    template_name = 'services_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'service_update.html'
    success_url = '/services/'
    #def get_success_url(self):
    #    return reverse_lazy('services', kwargs={'pk': self.object.pk})

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_delete.html'
    success_url = '/services/'