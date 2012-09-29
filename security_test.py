__author__ = 'backslash'

from pysuperfaktura import client, invoice, SFClient

api_client = SFClient.SFClient('blabla', 'blablablapapagaj')
#pdf_moja = client.get_pdf("88595","0")
#f = open('c:\\temp\\invoice_moja.pdf','wb+')
#f.write(pdf_moja)
#f.close()
#
#pdf_cudzia = client.get_pdf("88594","0")
#f = open('c:\\temp\\invoice_cudzia.pdf','wb+')
#f.write(pdf_cudzia)
#f.close()

#for i in range(88594,88596):
#    pdf_cudzia = client.get_pdf(str(i),"0")
#    f = open('c:\\temp\\'+str(i)+'-new2.pdf','wb+')
#    f.write(pdf_cudzia)
#    f.close()

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
client = client.Client(client_params)
item = invoice.SFInvoiceItem(item_params)
invoice = invoice.SFInvoice(client,invoice_params,[item])

print api_client.create_invoice(invoice)

