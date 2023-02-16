from unittest import TestCase
from get_request import get_request


class Test(TestCase):
    def test_get_request(self):
        self.assertEqual(get_request('https://test.te'), 0)
        self.assertEqual(get_request("https://greenatom.ru").status_code, 200)



