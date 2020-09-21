from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse

class SnackTest(SimpleTestCase):


    def status_code(self,page_name):
        expected = 200
        url = reverse(page_name)
        response = self.client.get(url)
        actual = response.status_code # Request to the application
        self.assertEquals(expected, actual)

    def page_template(self,page_name):
        url = reverse(page_name)
        response = self.client.get(url)
        actual = page_name + '.html'
        self.assertTemplateUsed(response, actual)
        self.assertTemplateUsed(response,'base-snaks.html')



    def test_home_page(self): 
        self.status_code('snacks-home')

    def test_about_page(self): 
        self.status_code('snacks-about')


    def test_templet_home_page(self): 
        self.page_template('snacks-home')

    def test_templet_about_page(self): 
        self.page_template('snacks-about')
