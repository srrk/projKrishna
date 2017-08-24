from xlsxwriter.workbook import Workbook
from io import BytesIO

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class SimpleTest(TestCase):
    def test_home_page_is_available(self):
        client = Client()
        url = reverse('index')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

    def test_the_view_for_invalid_file_upload(self):
        client = Client()
        url = reverse('index')
        f = SimpleUploadedFile("file.txt", b"file_content")
        response = self.client.post(url,{'file': f})
        self.assertContains(response, '<p>In-valid Excel File uploaded</p>', status_code=200)

    def test_the_view_for_valid_file_upload(self):
        client = Client()
        url = reverse('index')

        # Prepare excel file in memory.
        # import pdb; pdb.set_trace()

        output = BytesIO()
        book = Workbook(output, {'in_memory': True})
        sheet = book.add_worksheet('DD and Cash')
        sheet.write(0, 0, 'c-dac')
        book.close()
        output.seek(0)

        f = SimpleUploadedFile("file.xls", output.read())
        response = self.client.post(url, {'file':f})
        self.assertContains(response, '<p>Valid Excel File uploaded</p>', status_code=200)
        
