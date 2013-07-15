from pysuperfaktura.invoice import SFInvoiceClient, SFInvoiceItem, SFInvoice

__author__ = 'backslash7 <lukas.stana@it-admin.sk>'
import unittest
from pysuperfaktura.SFClient import SFClient

LOGIN = 'YOUR LOGIN HERE!'
APIKEY = 'YOUR API KEY HERE!'


class CreateTest(unittest.TestCase):
    def setUp(self):
        self.client = SFClient(LOGIN, APIKEY)

    def testCreateInvoice(self):
        client_params = {
            'name': 'Janko Hrasko',
            'ico': '12345678',
            'dic': '12345678',
            'ic_dph': 'SK12345678',
            'email': 'janko@hrasko.sk',
            'address': 'adresa',
            'city': 'mesto',
            'zip': 'psc',
            'phone': 'telefon',
        }

        invoice_params = {
            'name': 'nazov faktury',
            'variable': '123456',
            'constant': '0308',
            'specific': '2013',
            'already_paid': True,
            'invoice_no_formatted': '2012001',
            'created': '2013-05-28',
            'delivery': '2013-05-28',
            'due': '2013-06-28',
            'comment': 'komentar',
        }

        item_params = {
            'name': 'Superfaktura.sk',
            'description': 'Clenstvo',
            'quantity': 1,
            'unit': 'ks',
            'unit_price': 40.83,
            'tax': 20
        }
        client = SFInvoiceClient(client_params)
        item = SFInvoiceItem(item_params)
        invoice = SFInvoice(client, invoice_params, [item])
        self.client.create_invoice(invoice)


if __name__ == "__main__":
    unittest.main()