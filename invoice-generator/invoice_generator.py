import os
from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import datetime

rate = 2950



# define bussinessdays for current month
now = datetime.datetime.now()
holidays = {datetime.date(now.year, 8, 14)}
businessdays = 0
for i in range(1, 32):
    try:
        thisdate = datetime.date(now.year, now.month, i)
    except(ValueError):
        break
    if thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6 
        businessdays += 1


# choose english as language
os.environ["INVOICE_LANG"] = "en"

client = Client('Luxer One')
provider = Provider('Lucas Clavero', bank_account='1234567890', bank_code='2010')
creator = Creator('Lucas Clavero')
daily_work_hours = 8
invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'
invoice.add_item(Item(businessdays, rate*daily_work_hours  , description="services"))
# invoice.add_item(Item(1, 500, description="bonus"))
# invoice.add_item(Item(50, 60, description="Item 3", tax=0))
# invoice.add_item(Item(5, 600, description="Item 4", tax=15))

pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)