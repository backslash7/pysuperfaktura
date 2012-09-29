__author__ = 'backslash7 <lukas.stana@it-admin.sk>'

from exceptions import SFAPIException

class SFInvoiceItem:
    def __init__(self, params):
        self.params = params

class SFInvoice:
    def __init__(self, client, params, items=None):
        self.client = client
        self.params = params
        self.items = items

    def add_item(self,item):
        if not isinstance(SFInvoiceItem,item):
            raise SFAPIException('Passed object is not SFInvoiceItem instance')
        else:
            if self.items:
                self.items.append(item)
            else:
                self.items = [item]
