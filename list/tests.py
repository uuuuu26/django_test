from django.test import TestCase
import unittest
from selenium import webdriver
from django.core.urlresolvers import resolve
from list.views import home_page
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your tests here.

class homePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        #expected_html = render_to_string("home.html")
        #self.assertEqual(response.content.decode(), expected_html)