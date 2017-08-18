from django.test import TestCase
from django.test import Client
from django.urls import reverse

# Create your tests here.
class SimpleTest(TestCase):
    def test_home_page_is_available(self):
        client = Client()
        url = reverse('index')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
