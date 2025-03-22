from django.test import TestCase
from django.urls import reverse, resolve
from services.views import (
    NewServiceCreateView, ServiceListView, ServiceDetailView, 
    ServiceUpdateView, ServiceDeleteView
)

class ServiceURLsTest(TestCase):
    
    def test_new_service_url_resolves(self):
        url = reverse('new_service')
        self.assertEqual(resolve(url).func.view_class, NewServiceCreateView)

    def test_services_list_url_resolves(self):
        url = reverse('services')
        self.assertEqual(resolve(url).func.view_class, ServiceListView)

    def test_service_detail_url_resolves(self):
        url = reverse('service_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ServiceDetailView)

    def test_service_update_url_resolves(self):
        url = reverse('service_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ServiceUpdateView)

    def test_service_delete_url_resolves(self):
        url = reverse('service_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ServiceDeleteView)
