from collections import OrderedDict
import copy


def same_cols(cols1, cols2):
    empty = {}
    for k, v in cols2.items():
        if k in cols1.keys():
            empty[k] = v
    print(empty)
    return empty


def same_mean(mit_col, cols1, cols2, ):
    for k2, v2 in cols2.items():
        if k2 not in mit_col:
            for k1, v1 in cols1.items():
                if isinstance(v2, str) and isinstance(v1, str) and v1 is not "" and v2 is not "":
                    if v2 == v1:
                        mit_col[k2] = v2
    return mit_col


def sorts(mean, a, b, ):
    a_copy = OrderedDict(copy.deepcopy(a))
    b_copy = OrderedDict(copy.deepcopy(b))
    mean_copy = OrderedDict(copy.deepcopy(mean))

    a_copy2 = OrderedDict(copy.deepcopy(a))
    b_copy2 = OrderedDict(copy.deepcopy(b))
    mean_copy2 = OrderedDict(copy.deepcopy(mean))

    for mk, mv in mean.items():
        if mv != "" and mv in a.values() and mv in b.values():
            for ok, ov in a.items():
                if ov != " " and ov == mv:
                    a_copy.move_to_end(ok, last=False)
                    b_copy.move_to_end(mk, last=False)
                    mean_copy.move_to_end(mk, last=False)

    for k, v in mean.items():

        if k in a.keys() and k in b.keys():
            a_copy.move_to_end(k, last=False)
            b_copy.move_to_end(k, last=False)
            mean_copy.move_to_end(k, last=False)
    #

    a_copy.update(a_copy2)
    b_copy.update(b_copy2)
    mean_copy.update(mean_copy2)

    return mean_copy, a_copy, b_copy

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
def get_cols(read_book, sheet_name):
    table = read_book.sheet_by_name(sheet_name.upper())
    y1 = table.col_values(2, start_rowx=2, end_rowx=None)
    y2 = table.col_values(3, start_rowx=2, end_rowx=None)
    return {k: y2[i] for i, k in enumerate(y1)}
def sqlStringM(inputTb1,outputTb2,inputCols,outpuCols):
    return " ".join([
        "insert into ",
        inputTb1,
        " (",
        ",".join(inputCols),
        ") select ",
        ",".join(outpuCols),
        " from ",
        outputTb2+"@tc"

    ])
def sql_select(inputTb1,inputCols,place):
    return " ".join([
        "select ",
        ",".join(inputCols),
        "from ",
        inputTb1+place
    ])


if __name__ == '__main__':
    a = OrderedDict({
        "123": "65464",
        "353": "12312",
        "45636546": "123",
        "bbb": "c",
        "ddd": "f",

    })

    b = OrderedDict({
        "ddllkjlkjllld": "fg23123",

        "ddllld": "fg",

        "123": "345",
        "222": "12312",
        "2223": "",
        "45636546": "123",

        "l": "c",
    })
    mean = same_cols(a, b)
    mean = OrderedDict(same_mean(mean, a, b, ))

    mean_copy, a_copy, b_copy = sorts(mean, a, b)
    print("a", a_copy)
    print("b", b_copy)
    print("mean", mean_copy)


