from django.test import TestCase

#test-driven ch3
class smokeTest(TestCase):
    
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)
