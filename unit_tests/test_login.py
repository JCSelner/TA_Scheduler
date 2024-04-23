from django.urls import reverse
from django.test import TestCase


class LoginTest(TestCase):
    def test_login_page_exist(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')
