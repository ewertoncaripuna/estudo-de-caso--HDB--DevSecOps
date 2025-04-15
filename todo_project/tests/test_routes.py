import sys
import os

# Adiciona o path do diretório interno correto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'todo_project')))

import unittest
from todo_project import app

class BasicRouteTests(unittest.TestCase):
    def setUp(self):
        # Usa a app já instanciada
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Desativa CSRF para facilitar o teste de forms
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 302])  # 302 se redirecionar pro login

    def test_login_route(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register_route(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

