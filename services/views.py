from services.models import Service
from services.forms import ServiceModelForm
from django.views.generic import CreateView
# Create your views here.

class NewServiceCreateView(CreateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'new_service.html'
    success_url = '/services/'
