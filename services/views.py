from services.models import Service
from services.forms import ServiceModelForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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