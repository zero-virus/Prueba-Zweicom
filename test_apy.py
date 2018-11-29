import json
import unittest

from prueba_zweicom import app

app.testing = True

class TestApi(unittest.TestCase):
	
	def test_main(self):
		with app.test_client() as client:
			sent = {'return_url': 'my_test_'}
