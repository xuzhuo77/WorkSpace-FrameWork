import xlrd

from synchronation.tool import sql_select, sqlStringM
a=[]


def get_col_Pairs(read_book, sheet_indx):
    table = read_book.sheet_by_index(sheet_indx)

    copyy1=y1 = table.col_values(0, start_rowx=0, end_rowx=None)
    y1=list(filter(lambda x:x!='',y1))
    if y1.count("表名")>=2:
        idxs=[ k for k,value in enumerate(copyy1) if "表名" in value]
        output={}
        for k,rowid in enumerate(idxs):
            try:
                end_row=idxs[k+1]
            except :
                end_row=None
            tb2 = table.cell_value(idxs[k], 1)
            tb3 = table.cell_value(idxs[k], 3)
            # if "中文" in tb3:
            #     continue
            y2=table.col_values(1, start_rowx=idxs[k]+2, end_rowx=end_row)
            y3=table.col_values(3, start_rowx=idxs[k]+2, end_rowx=end_row)




            output[i]=[tb2,tb3,y2,y3]
        return output

    else:

        tb2= table.cell_value(0,1)
        tb3= table.cell_value(0,3)
        if "中文" in tb3:
            return False
        y2 = table.col_values(1, start_rowx=2, end_rowx=None)
        # y2 = list(filter(lambda x: x != '', y2))

        y3 = table.col_values(3, start_rowx=2, end_rowx=None)
        # y3=list(filter(lambda x:x!='',y3))

        # print(len(y1),len(y2))
        # print(y2,y3)
        return {1:[tb2,tb3,y2,y3]}
    # itr_len =enumerate(y2) if len(y1)>len(y2) else enumerate(y1)


workbook = xlrd.open_workbook("文书未生成表.xls")  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。

sqlStr=[]
for i in range(workbook.nsheets):
    dict=get_col_Pairs(workbook,i)
    if dict:
        for t in dict.values():
            tb1, tb2, y1, y2=t

            print(sql_select(tb1,y1))
            print(sql_select(tb2,y2))
        # print(col_ids)
            sqlStr.append(sqlStringM(tb1,tb2,y1,y2))
for k in sqlStr:

    print(k)

