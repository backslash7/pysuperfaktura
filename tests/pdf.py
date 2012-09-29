__author__ = 'backslash7 <lukas.stana@it-admin.sk>'
import unittest
from pysuperfaktura.SFClient import SFClient
from pysuperfaktura.exceptions import SFAPIException

LOGIN = 'YOUR LOGIN HERE!'
APIKEY = 'YOUR API KEY HERE!'

class GetPDFTest(unittest.TestCase):
    def setUp(self):
        self.client = SFClient(LOGIN,APIKEY)

    def testGetPdf(self):
        self.assertRaises(SFAPIException,self.client.get_pdf,"0","0")
if __name__ == "__main__":
    unittest.main()
