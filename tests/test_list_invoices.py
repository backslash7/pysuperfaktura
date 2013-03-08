__author__ = 'backslash7 <lukas.stana@it-admin.sk>'
import unittest
from pysuperfaktura.SFClient import SFClient

LOGIN = 'lukas.stana@it-admin.sk'
APIKEY = 'c99f792ffaebe15d0d392075b288df9e'


class GetPDFTest(unittest.TestCase):
    def setUp(self):
        self.client = SFClient(LOGIN, APIKEY)

    def testListAllInvoices(self):
        self.assertGreater(len(self.client.list_invoices()), 0)

    def testListuserInvoices(self):
        self.assertGreater(len(self.client.list_invoices(params={'client_id': '90827'})), 0)


if __name__ == "__main__":
    unittest.main()