pysuperfaktura
==============

Python API connector pre projekt superfaktura.sk

Inštalácia
----------
    pip install https://github.com/backslash7/pysuperfaktura/archive/master.zip

Vytvorenie faktúry
------------------
```python
from pysuperfaktura.SFClient import SFClient
from pysuperfaktura.invoice import SFInvoiceClient, SFInvoice, SFInvoiceItem,

api_client = SFClient('jar-jar@binks.net', 'meesahungry') // Použite svoj SF login a API key
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
    'specific': '2012',
    'already_paid': True,
    'invoice_no_formatted': '2012001',
    'created': '2012-03-28',
    'delivery': '2012-03-28',
    'due': '2012-03-28',
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
invoice = SFInvoice(client,invoice_params,[item])
client.create_invoice(invoice)
```
