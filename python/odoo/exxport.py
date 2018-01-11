def export(filename, datas, sheets):
   book_wr = xlwt.Workbook()
   for sheet in sheets:
       sh = book_wr.add_sheet(sheet['name'])
       index = 0
       for title in sheet['title']:
           sh.write(0, index, title)
           index += 1
       i = 1
       for data in datas[sheet['name']]:
           j = 0
           for field in sheet['field']:
               sh.write(i, j, data[field])
               j += 1
           i += 1

   book_wr.save(filename)
