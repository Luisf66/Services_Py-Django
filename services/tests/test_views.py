from django.test import TestCase, Client
from django.urls import reverse
from services.models import Service

class ServiceViewsTest(TestCase):
    def setUp(self):
        """Configuração inicial para os testes"""
        self.client = Client()

        # Criar um serviço para testar as views de detalhe, atualização e exclusão
        self.service = Service.objects.create(
            name="Teste Service",
            description="Descrição de teste",
            price=100.0
        )

    def test_new_service_create_view_get(self):
        """Testa se a página de criação de serviço carrega corretamente"""
        response = self.client.get(reverse('new_service'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_service.html')

    def test_new_service_create_view_post(self):
        """Testa a criação de um novo serviço via POST"""
        response = self.client.post(reverse('new_service'), {
            'name': 'ServicoTeste123',
            'description': 'Descrição do novo serviço',
            'price': 150.0
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertEqual(Service.objects.count(), 2)  # Agora existem 2 serviços

    def test_services_list_view(self):
        """Testa se a lista de serviços é carregada corretamente"""
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services_list.html')
        self.assertContains(response, self.service.name)  # Verifica se o nome do serviço está na página

    def test_service_detail_view(self):
        """Testa se o detalhe de um serviço específico é carregado corretamente"""
        response = self.client.get(reverse('service_detail', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_detail.html')
        self.assertContains(response, self.service.name)  # Verifica se o nome do serviço está na página

    def test_service_update_view_get(self):
        """Testa se a página de edição de serviço carrega corretamente"""
        response = self.client.get(reverse('service_update', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_update.html')

    def test_service_update_view_post(self):
        """Testa a atualização de um serviço via POST"""
        response = self.client.post(reverse('service_update', kwargs={'pk': self.service.pk}), {
            'name': 'Servico Atualizado',
            'description': self.service.description,
            'price': self.service.price
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após atualização
        self.service.refresh_from_db()
        self.assertEqual(self.service.name, 'Servico Atualizado')  # Verifica se o nome foi atualizado

    def test_service_delete_view(self):
        """Testa a exclusão de um serviço"""
        response = self.client.post(reverse('service_delete', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, 302)  # Redireciona após exclusão
        self.assertEqual(Service.objects.count(), 0)  # O serviço foi deletado
