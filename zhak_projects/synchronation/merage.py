
from  collections import OrderedDict,Counter
table1={"xyz":1,
        "abc":2,

        }
table2={"xyz":2,
        "xxxxx":3}



def same_table_name(table1,table2):
    l=[]
    for t, (k, v) in enumerate(table2.items()):
        if k in table1.keys():
            l.append(k)
    return l


same_table_name(table1,table2)

cols1=OrderedDict({
    "123":1,
    "456":8,
    "xyz":0
})

cols2=OrderedDict({
    "123":1,
    "bbb": 89,
    "456":0,
    "kkk":90
})

# cols2.__reversed__()
reversed(cols2)
print(cols2)

def same_cols(cols1,cols2):
    empty = {}
    for k, v in cols2.items():
        if k in cols1.keys():
            empty[k] = v
    print(empty)
    return empty


mid_col=same_cols(cols1,cols2)
def same_mean(cols1,cols2,mit_col):

    for k, v in cols2.items():
        if k not in mit_col:
            for k1,v1 in cols1.items():
                if isinstance(v ,str ) and isinstance(v1,str):
                    if v == v1:
                        mid_col[k]=v
    return mit_col
mid_col=same_mean(cols1,cols2,mid_col)

import xlwt

COL_START=4 # 起始列
ROW_START=4 # 起始行
import copy
def compare_col_sheet(workbook,table_name,mid_col,cols1,cols2):
    worksheet = workbook.add_sheet(table_name)
    worksheet.write(0, 0, table_name)


    output_col1={}
    compare_col={}
    output_col2={}
    w={}
    for i, (midk, mikv) in enumerate(mid_col.items()):

        if midk in cols1.keys() and midk in cols2.keys():
            output_col1[midk]=mikv
            compare_col[midk]=mikv
            output_col2[midk] = mikv

    print(2,Counter(compare_col))

    diff_col ={ k:v for k, v in mid_col.items()if k not in compare_col.keys()}

    i=0
    x=[]
    # diff_col=dict(Counter(mid_col)-Counter(compare_col))
    for i, (mid_key, mid_val) in enumerate(diff_col.items()):
            if diff_col[mid_key] in cols1.values() and diff_col[mid_key] in cols2.values():
                for k1,v1 in cols1.items():
                        if v1==diff_col[mid_key] and mid_key!=k1:
                                i+=1
                                output_col1[k1+str(i)] = v1
                                compare_col[mid_key] = mid_val
                                output_col2[mid_key] = mid_val

                    
    compare_col.update(w)
    output_col1.update(cols1)
    output_col2.update(cols2)



    cols1_copy=output_col1
    cols2_copy=output_col2
    mid_col_copy=compare_col
    


    for i, (cl1k, cl1v) in enumerate(mid_col_copy.items()):
        worksheet.write(ROW_START + i, COL_START + 2, cl1k)
        worksheet.write(ROW_START + i, COL_START + 3, mid_col[cl1k])

    for i, (cl1k, cl1v) in enumerate(cols1_copy.items()):
        worksheet.write(ROW_START + i, COL_START, cl1k)
        worksheet.write(ROW_START + i, COL_START + 1, cl1v)

    for i, (cl2k, cl2v) in enumerate(cols2_copy.items()):
        if cl2k not in mid_col.keys():
            worksheet.write(ROW_START + i, COL_START + 4, cl2k)
            worksheet.write(ROW_START + i, COL_START + 5, cl2v)

    worksheet.col(COL_START+1).width = 6000
    worksheet.col(COL_START+2).width = 6000

    worksheet.col(COL_START+3).width = 6000

    worksheet.col(COL_START+4).width = 6000
    worksheet.col(COL_START).width = 6000






# import  xlrd
# workbook = xlrd.open_workbook('aaa.xls')#文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
# for sheet_indx in range(workbook.nsheets):
#     table = workbook.sheet_by_index(sheet_indx) #通过索引顺序获取
#
#     # nrows = table.nrows  # 获取该sheet中的有效行数
#     # for i in range(4):
#     inputCol=table.col_values(COL_START,start_rowx=ROW_START,end_rowx=None)
#     outpuCol=table.col_values(COL_START+2,start_rowx=ROW_START,end_rowx=None)
#     tablename=table.cell_value(0,0)
#     sqlStr_list=[
#     "insert into ",
#     tablename+"@sydb",
#     " (",
#     ",".join(inputCol),
#     ") select ",
#     ",".join(outpuCol),
#     ]
#     # print(sqlStr_list)
#     sqlStr=" ".join(sqlStr_list)
#
#     print(sqlStr)




from synchronation.readfiles import JavaGetOld
from synchronation.readNewModel import JavaGetNew
new_models=JavaGetNew()
old_models=JavaGetOld()

# workbook = xlwt.Workbook()
# compare_col_sheet(workbook,"k",mid_col)
# workbook.save('aaa.xls')

ol={list(o.table.keys())[0].lower():o.table[list(o.table.keys())[0]] for o in old_models }
nl={list(o.table.keys())[0].lower():o.table[list(o.table.keys())[0]] for o in new_models if o.table.keys()}


print(ol)
print(nl)
nl=OrderedDict(nl)
ol=OrderedDict(ol)
mid_col=same_cols(nl,ol)
mid_col=same_mean(nl,ol,mid_col)
mid_table=OrderedDict(mid_col)


workbook = xlwt.Workbook()
compare_col_sheet(workbook,"k",mid_table,nl,ol)
workbook.save('same_table_name.xls')


