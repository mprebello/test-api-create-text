from django.test import TestCase, Client
from django.conf import settings
import os

class AddTextViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = 'f{settings.URL_PATH}/{settings.URL_PATH_FUNCTION_ADD_TEXT}/'
        self.test_text = 'Hello, World!'
        self.file_path = settings.FILE_DESTINATION

        # Ensure the file is empty before each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_text_view_status_code(self):
        response = self.client.get(self.url, {settings.URL_PATH_FUNCTION_ADD_TEXT_VAR: self.test_text})
        self.assertEqual(response.status_code, 200)

    def test_add_text_view_content(self):
        response = self.client.get(self.url, {settings.URL_PATH_FUNCTION_ADD_TEXT_VAR: self.test_text})
        self.assertIn(self.test_text, response.content.decode())

    def test_text_written_to_file(self):
        self.client.get(self.url, {settings.URL_PATH_FUNCTION_ADD_TEXT_VAR: self.test_text})
        with open(self.file_path, 'r') as file:
            content = file.read()
            self.assertIn(self.test_text, content)

    def test_empty_text_not_written_to_file(self):
        self.client.get(self.url, {settings.URL_PATH_FUNCTION_ADD_TEXT_VAR: ''})
        with open(self.file_path, 'r') as file:
            content = file.read()
            self.assertEqual(content, '')
