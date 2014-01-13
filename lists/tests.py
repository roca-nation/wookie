from django.test import TestCase
from django.core.urlresolvers import resolve #ch3.2
from lists.views import home_page #ch3.2

#test-driven ch3.1
#class smokeTest(TestCase):
    
    #def test_bad_maths(self):
        #self.assertEqual(1+1, 3)

#ch3.2
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)








