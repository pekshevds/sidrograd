from django.test import TestCase
from index_app.models import ContactInfo, TypeOfContactInfo
from api_app.services import process_call_back_data


class SendMessageTestCase(TestCase):
    def setUp(self) -> None:
        self._email1 = ContactInfo.objects.create(
            type=TypeOfContactInfo.EM, value="info@sidrograd.ru"
        )
        self._data1 = {
            "subject": "info@sidrograd.ru",
            "tel": "",
            "link": "",
        }

    def test_send_message(self) -> None:
        self.assertEqual(process_call_back_data(self._data1), 1)
