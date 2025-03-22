from django.test import TestCase
from django.core.exceptions import ValidationError
from services.models import Service

class ServiceModelTest(TestCase):

    def test_create_service(self):
        """Testa a criação de um serviço válido"""
        service = Service.objects.create(
            name="Manutenção de Computador",
            description="Serviço completo de manutenção e limpeza.",
            price=150.0
        )
        self.assertIsNotNone(service.id)
        self.assertEqual(service.name, "Manutenção de Computador")
        self.assertEqual(service.description, "Serviço completo de manutenção e limpeza.")
        self.assertEqual(service.price, 150.0)

    def test_service_str_method(self):
        """Testa a representação do serviço como string"""
        service = Service.objects.create(
            name="Jardinagem",
            description="Manutenção de jardim e poda de plantas.",
            price=80.0
        )
        self.assertEqual(str(service), "Jardinagem")

    def test_name_max_length(self):
        """Testa se o nome respeita o limite de caracteres"""
        long_name = "A" * 101  # Nome com 101 caracteres (limite é 100)
        service = Service(name=long_name, description="Teste", price=20.0)
        
        with self.assertRaises(ValidationError):
            service.full_clean()

    def test_blank_description(self):
        """Testa se a descrição pode ser vazia"""
        service = Service.objects.create(name="Corte de Cabelo", description="", price=30.0)
        self.assertEqual(service.description, "")

    def test_price_decimal(self):
        """Testa se o preço suporta valores decimais corretamente"""
        service = Service.objects.create(name="Aula de Música", description="Aula particular de violão", price=99.99)
        self.assertEqual(service.price, 99.99)
