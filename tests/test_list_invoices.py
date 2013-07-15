__author__ = 'backslash7 <lukas.stana@it-admin.sk>'
import unittest
from pysuperfaktura.SFClient import SFClient

LOGIN = 'YOUR LOGIN HERE!'
APIKEY = 'YOUR API KEY HERE!'


class ListTest(unittest.TestCase):
    def setUp(self):
        self.client = SFClient(LOGIN, APIKEY)

    def testListAllInvoices(self):
        self.assertGreater(len(self.client.list_invoices()), 0)

    def testListClientsInvoices(self):
        self.assertGreater(len(self.client.list_invoices_by_client(90827)), 0)

    def testListDueInvoices(self):
        self.assertGreater(len(self.client.list_due_invoices()), 0)

    def testListUnpaidInvoices(self):
        self.assertGreater(len(self.client.list_unpaid_invoices()), 0)

    def testListPartiallyPaidInvoices(self):
        self.assertGreater(len(self.client.list_partially_paid_invoices()), 0)

    def testListPaidInvoices(self):
        self.assertGreater(len(self.client.list_paid_invoices()), 0)


if __name__ == "__main__":
    unittest.main()