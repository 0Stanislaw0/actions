from django.test import TestCase

class YourTestClass(TestCase):
    '''
hellop

    '''
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        # hee
        b_a = False
        self.assertFalse(b_a)

    def test_something_that_will_fail(self):
        # ww
        a_b = True
        self.assertTrue(a_b)
