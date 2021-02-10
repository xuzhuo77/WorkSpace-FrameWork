

import xlrd
def get_colsById(read_book, sheet_indx):
    table = read_book.sheet_by_index(sheet_indx)
    y1 = table.col_values(4, start_rowx=4, end_rowx=None)
    y2 = table.col_values(6, start_rowx=4, end_rowx=None)
    y1=list(filter(lambda x:x!='',y1))
    y2=list(filter(lambda x:x!='',y2))
    tb1= table.cell_value(0,4)
    tb2= table.cell_value(0,6)
    print(len(y1),len(y2))
    itr_len =enumerate(y2) if len(y1)>len(y2) else enumerate(y1)

    return tb1,tb2,{k: y2[i] for i, k in itr_len}



workbook = xlrd.open_workbook('write.xls')  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。

sqlStr=[]
for i in range(workbook.nsheets):
    tb1,tb2,col_ids=get_colsById(workbook,i)
    # print(sql_select(tb1,col_ids.keys()))
    # print(sql_select(tb2,col_ids.values()))
    # print(col_ids)
    # sqlStr.append(sqlStringM(tb1,tb2,col_ids.keys(),col_ids.values()))
for k in sqlStr:

    print(k)



