__author__ = 'backslash7 <lukas.stana@it-admin.sk>'

import json
from StringIO import StringIO

import requests

from exceptions import SFAPIException

from invoice import SFInvoice


class SFClient:
    sfapi_base_url = 'https://moja.superfaktura.sk'
    getpdf_url = '/invoices/pdf/'
    create_invoice_url = '/invoices/create/'
    list_invoices_url = '/invoices/index.json'

    def __init__(self, email, apikey):
        self.email = email
        self.apikey = apikey
        self.auth_header = {'Authorization': "".join(['SFAPI ', 'email=', self.email, '&apikey=', self.apikey])}

    def create_invoice(self, invoice):
        if isinstance(invoice, SFInvoice):
            data = {'Client': invoice.client.params, 'Invoice': invoice.params, 'InvoiceItem': []}
            for item in invoice.items:
                data['InvoiceItem'].append(item.params)
            url = "".join([self.sfapi_base_url, self.create_invoice_url])
            req = requests.post(url, data={'data': json.dumps(data)}, headers=self.auth_header)
            if req.status_code == requests.codes.ok:
                return json.loads(req.text)
            else:
                raise SFAPIException('Creating invoice failed! Status code: %d' % req.status_code)
        else:
            raise SFAPIException('Passed invoice is not SFInvoice instance!')

    def get_pdf(self, invoice_id, token):
        url = "".join([self.sfapi_base_url, self.getpdf_url, invoice_id, '/token:', token])
        req = requests.get(url, headers=self.auth_header)
        if req.status_code == requests.codes.ok:
            handle = StringIO(req.content)
            if handle.read(4) != '%PDF':
                raise SFAPIException('Returned document does not look like PDF file')
        else:
            raise SFAPIException('PDF retrieval failed! Status code: %d' % req.status_code)

    def list_invoices(self, params=None):
        filter_url = []
        if params:
            for (k, v) in params.items():
                filter_url.append("".join(['/', k, ':', v]))

        url = "".join([self.sfapi_base_url, self.list_invoices_url, "".join(filter_url) if filter_url else ""])
        req = requests.get(url, headers=self.auth_header)
        if req.status_code != requests.codes.ok:
            raise SFAPIException('Listing invoices failed! Status code: %s' % req.status_code)

        response = json.loads(req.text)
        return response
