# coding=utf-8

__author__ = 'backslash7 <lukas.stana@it-admin.sk>'

import json
import requests
from exceptions import SFAPIException
from invoice import SFInvoice, SFInvoiceClient


class SFClient:
    sfapi_base_url = 'https://moja.superfaktura.sk'
    getpdf_url = '/invoices/pdf/'
    create_invoice_url = '/invoices/create/'
    list_invoices_url = '/invoices/index.json'

    def __init__(self, email, api_key):
        """
        Inicializuje inštanciu
        :param email: email ako login
        :param api_key: API KEY pre komunikáciu so SF
        """
        self.email = email
        self.api_key = api_key
        self.auth_header = {'Authorization': "".join(['SFAPI ', 'email=', self.email, '&apikey=', self.api_key])}

    def construct_filter(self, params):
        """
        Vytvor filter string použiteľný v URL na základe zadaného slovníka
        :param params:
        :return: string vygenerovaný zo slovníka
        """
        if not isinstance(params, dict):
            raise SFAPIException('Filter parameters must be a dictionary')
        filter_url = []
        for (k, v) in params.items():
            filter_url.append("".join(['/', k, ':', str(v)]))

        return "".join(filter_url)

    def send_request(self, action, method='GET', data=None, filter=None, json_output=True):
        """Zašle request pre SF API
        :param action: URL akcie
        :type action: basestring
        :param method: HTTP metóda (GET alebo POST)
        :type method: basestring
        :param data: Dodatočné dáta posielané na SF API
        :type data: dict
        :param filter: Reťazec filtrovania výsledku
        :type filter: basestring
        :param json_output: Indikuje, či je výsledok interpretovaný ako JSON dáta
        :type json_output: bool
        :return: Dáta získané z SF API v stanovenom formáte (JSON/RAW)
        :type return: dict/basestring
        :raise: SFAPIException v prípade, že SF API odpovedalo chbovým HTTP status kódom
        """
        url_portions = [self.sfapi_base_url, action]
        if filter:
            url_portions.append(filter)
        url = "".join(url_portions)
        req = requests.request(method, url, data=data, headers=self.auth_header)
        if req.status_code != requests.codes.ok:
            error_data = {
                'method': method,
                'action': action,
                'code': req.status_code
            }
            raise SFAPIException('%(method)s on %(action)s failed with status code %(code)d' % error_data)
        if json_output:
            returned_string = json.loads(req.text)
            if 'error' in returned_string and returned_string['error'] == 1:
                raise SFAPIException('Error while creating invoice %(error_message)s' % returned_string)
            else:
                return returned_string
        else:
            return req.content

    def create_invoice(self, invoice):
        """
        Vytvorí v SF faktúru
        :param invoice: Objekt faktúry
        :type invoice: SFInvoice
        :return: :raise:
        """
        if not isinstance(invoice, SFInvoice):
            raise SFAPIException('Passed invoice is not SFInvoice instance!')

        data = {'Client': invoice.client.params, 'Invoice': invoice.params, 'InvoiceItem': []}
        for item in invoice.items:
            data['InvoiceItem'].append(item.params)

        return self.send_request(self.create_invoice_url, method='POST', data={'data': json.dumps(data)})

    def get_pdf(self, invoice_id, token):
        """

        :param invoice_id:
        :param token:
        :return:
        """
        return self.send_request("".join([self.getpdf_url, invoice_id, '/token:', token]), json_output=False)

    def list_invoices(self, params=None):
        """

        :param params:
        :return:
        """
        filter_url = ""
        if params:
            filter_url = self.construct_filter(params)
        returned_invoices = self.send_request(self.list_invoices_url, filter=filter_url)
        invoice_list = []
        if len(returned_invoices) != 0:
            for returned_invoice in returned_invoices:
                returned_client = json.loads(returned_invoice['Invoice'].pop('client_data'))
                client = SFInvoiceClient(returned_client['Client'])
                # TODO: SF namiesto poľa položiek vráti takýto blbý string:
                #  u'items_data': u'Item1, Item2, ',
                returned_items = []
                invoice = SFInvoice(client, returned_invoice, returned_items)
                invoice_list.append(invoice)

            return invoice_list

    def list_invoices_by_client(self, client_id):
        """

        :param client_id:
        :return:
        """
        return self.list_invoices(params={'client_id': client_id})

    def list_due_invoices(self):
        """


        :return:
        """
        return self.list_invoices(params={'status': '99'})

    def list_unpaid_invoices(self):
        """


        :return:
        """
        return self.list_invoices(params={'status': '1'})

    def list_partially_paid_invoices(self):
        """


        :return:
        """
        return self.list_invoices(params={'status': '2'})

    def list_paid_invoices(self):
        """


        :return:
        """
        return self.list_invoices(params={'status': '3'})
