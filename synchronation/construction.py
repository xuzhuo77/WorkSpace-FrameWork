from collections import OrderedDict
import re
import xlrd
import copy
import xlwt

from synchronation.tool import sorts, same_cols, same_mean, get_cols

COL_START = 4  # 起始列
ROW_START = 4  # 起始行


# def same_cols(cols1,cols2):
#     empty = {}
#     for k, v in cols2.items():
#         if k in cols1.keys():
#             empty[k] = v
#     print(empty)
#     return empty
#
#
# def same_mean(mit_col,cols1,cols2):
#
#     for k, v in cols2.items():
#         if k not in mit_col:
#             for k1,v1 in cols1.items():
#                 if isinstance(v ,str ) and isinstance(v1,str):
#                     if v == v1:
#                         mid_col[k]=v
#     return mit_col


def compare_col_sheet(mid_col, cols1, cols2):
    cols1_copy = OrderedDict(copy.deepcopy(cols1))
    cols2_copy = OrderedDict(copy.deepcopy(cols2))
    mid_col_copy = OrderedDict(copy.deepcopy(mid_col))
    hava = {}
    for i, (mid_key, mid_value) in enumerate(mid_col.items()):
        if mid_key in cols1.keys() and mid_key in cols2.keys():
            cols1_copy.move_to_end(mid_key, last=False)
            cols2_copy.move_to_end(mid_key, last=False)
            mid_col_copy.move_to_end(mid_key, last=False)
            hava[mid_key] = mid_value

    diff_col = {k: v for k, v in mid_col.items() if k not in hava.keys()}

    # diff_col=dict(Counter(mid_col)-Counter(compare_col))
    for i, (mid_key, mid_val) in enumerate(diff_col.items()):
        if diff_col[mid_key] in cols1.values() and diff_col[mid_key] in cols2.values():
            for k1, v1 in cols1.items():
                if v1 == diff_col[mid_key] and mid_key != k1:
                    cols1_copy.move_to_end(mid_key, last=False)
                    cols2_copy.move_to_end(mid_key, last=False)
                    mid_col_copy.move_to_end(mid_key, last=False)

    return mid_col_copy, cols1_copy, cols2_copy


def save_sheet(worksheet, mid_col, cols1, cols2):
    for i, (cl1k, cl1v) in enumerate(mid_col.items()):
        worksheet.write(ROW_START + i, COL_START + 2, cl1k)
        worksheet.write(ROW_START + i, COL_START + 3, mid_col[cl1k])

    for i, (cl1k, cl1v) in enumerate(cols1.items()):
        worksheet.write(ROW_START + i, COL_START, cl1k)
        worksheet.write(ROW_START + i, COL_START + 1, cl1v)

    for i, (cl2k, cl2v) in enumerate(cols2.items()):
        if cl2k not in mid_col.keys():
            worksheet.write(ROW_START + i, COL_START + 4, cl2k)
            worksheet.write(ROW_START + i, COL_START + 5, cl2v)

    worksheet.col(COL_START + 1).width = 6000
    worksheet.col(COL_START + 2).width = 6000

    worksheet.col(COL_START + 3).width = 6000

    worksheet.col(COL_START + 4).width = 6000
    worksheet.col(COL_START).width = 6000


workbook = xlrd.open_workbook('same_table_name.xls')  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
for sheet_indx in range(workbook.nsheets):
    table = workbook.sheet_by_index(sheet_indx)  # 通过索引顺序获取

    y1 = table.col_values(4, start_rowx=4, end_rowx=None)
    y2 = table.col_values(6, start_rowx=4, end_rowx=None)

    y2 = list(filter(lambda x: x != "", y2))
    y1 = y1[:len(y2)]

    y1 = [re.compile("[^0-9]+").findall(y)[0] for y in y1]
    newworkbook = xlrd.open_workbook('newModel.xls')  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
    oldworkbook = xlrd.open_workbook('oldModel.xls')  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
    writeInworkbook = xlwt.Workbook()

    idx = 0
    for i, y in enumerate(y1):
        nd = OrderedDict(get_cols(newworkbook, y1[i]))
        od = OrderedDict(get_cols(oldworkbook, y2[i]))

        mid_col = same_cols(nd, od)
        mid_col = same_mean(mid_col, nd, od)
        mid_table = OrderedDict(mid_col)

        mid_col, nd, od = sorts(mid_col, nd, od)
        try:
            write_sheet = writeInworkbook.add_sheet(y1[i].upper())
        except:
            write_sheet = writeInworkbook.add_sheet(y1[i] + str(idx).upper())
            idx += 1



        save_sheet(write_sheet, mid_col, nd, od)
        write_sheet.write(0 , COL_START , y1[i])
        write_sheet.write(0 , COL_START + 2, y2[i])


    writeInworkbook.save('write.xls')
