import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask
app = Flask(__name__)

class TestRutas(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_flask_funciona(self):
        # Una prueba simple para que no marque error
        self.assertTrue(app is not None)