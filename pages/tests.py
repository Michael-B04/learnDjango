#python has built-in testing framework called unittest
#Django test framework is on top of unittest (Pythons lib
#four test cases, simpletestcase, testcase, transactiontestcase, Liveservertestcase)

#from django.test import TestCase
from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code,200)