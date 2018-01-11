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
Branch: master Find file Copy pathodoo/export_product.py
f5e943a  on 10 Oct, 2017
@12t4bkdn 12t4bkdn Create export_product.py
1 contributor
RawBlameHistory     
62 lines (47 sloc)  1.51 KB
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

book_wr = xlwt.Workbook()
for sheet in book.sheets():
    sh = book_wr.add_sheet(sheet.name)
    print sheet.name
    sh.write(0, 0, 'Barcode')
    sh.write(0, 1, 'Qty')
    index = 1
    for i in range(1, sheet.nrows):
        barcode = formatCharValue(sheet.cell(i, 0).value)
        qty = formatCharValue(sheet.cell(i, 1).value)
        product = sock.execute(DB, uid, PASS, 'product.product', 'search', [('ean13', '=', barcode)]);
        if product is list:
            print barcode
            sh.write(index, 0, barcode)
            sh.write(index, 1, qty)
            index += 1

book_wr.save(savepath)


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
