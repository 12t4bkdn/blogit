Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Explore
 @12t4bkdn
 Sign out
 Watch 0
  Star 0  Fork 0 12t4bkdn/odoo
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
Branch: master Find file Copy pathodoo/import_inventory_adjustment.py
a9564d0  on 10 Oct, 2017
@12t4bkdn 12t4bkdn Update import_inventory_adjustment.py
1 contributor
RawBlameHistory     
72 lines (55 sloc)  2.08 KB
import xmlrpclib
import json
import xlrd
import xlwt
# from xlrd import open_workbook

DB   = 'onemart**'
USER = '*****'
PASS = '*****'

ROOT = 'http://onemartv7.equiperp.com/xmlrpc/'

uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid: %d)" % (USER, uid)

sock = xmlrpclib.ServerProxy(ROOT + 'object')
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(ROOT))

table = 'product.template'
fields = sock.execute(DB, uid, PASS, table, 'fields_get', [])

path = 'Stock Count 6th Oct.xlsx'
savepath = 'none_exist20171009.xlsx'


def formatCharValue(value):
    try:
        return str(int(value))
    except Exception:
        pass
    return value

def getTaxId(value):
    tax_ids =  sock.execute(DB, uid, PASS, 'account.tax', 'search', [('amount', '=', value)]);
    if type(tax_ids) is list:
        return tax_ids[0]
    return 0

# Open the workbook
book = xlrd.open_workbook(path)

for sheet in book.sheets():
    print sheet.name
    quantity = {}
    unique_barcode = []
    for i in range(1, sheet.nrows):
        barcode = formatCharValue(sheet.cell(i, 0).value)
        qty = formatCharValue(sheet.cell(i, 1).value)
        if barcode not in unique_barcode:
            unique_barcode.append(barcode)
            quantity[barcode] = qty
        else:
            quantity[barcode] += qty
    product_list = []
    for barcode in unique_barcode:
        product_ids = sock.execute(DB, uid, PASS, 'product.product', 'search', [('ean13', '=', barcode)]);
        if product_ids:
            product_list.append([0, 0, {'product_id': product_ids[0],
                                    'location_id': 12,
                                    'product_qty': quantity[barcode]}])

    sock.execute(DB, uid, PASS, 'stock.inventory', 'create', {'name': 'Stock Count 6th Oct - ' + sheet.name,
                                                    'location_id': 12,
                                                    'filter': 'partial',
                                                    'line_ids': product_list,
                                                    })
    pass




© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
About
