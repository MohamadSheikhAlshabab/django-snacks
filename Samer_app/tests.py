from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class AppTest(SimpleTestCase):
    def test_home_status_code(self):
        expected = 200
        url = reverse('samerhome')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_about_status_code(self):
        expected = 200
        url = reverse('samerabout')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_about_page_template(self):
        url = reverse('samerabout')
        response = self.client.get(url)
        actual = 'samer_about.html'
        self.assertTemplateUsed(response , actual)

    def test_home_page_template(self):
        url = reverse('samerhome')
        response = self.client.get(url)
        actual = 'samer_home.html'
        self.assertTemplateUsed(response , actual)
