from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class AppTest(SimpleTestCase):
    def test_home_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_about_status_code(self):
        expected = 200
        url = reverse('about')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        actual = 'snacks-about.html'
        self.assertTemplateUsed(response , actual)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'snacks-home.html'
        self.assertTemplateUsed(response , actual)



    
