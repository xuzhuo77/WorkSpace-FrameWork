import xlwt
import os
import re

New_readfile_path = "D:\\ideaworkspace\\safety\\safety-inspection-service\\src\\main\\java\\com\\lsh\\agg\\safety\\inspection\\model"
New_readfile_path = "D:\\ideaworkspace\\safety\\safety-emergency-supplies-service\\src\\main\\java\\com\\lsh\\agg\\safety\\emergency\\supplier\\model"
example_file = 'zjkCity_Menu.java'
example_file = 'DocNewFzscyjs.java'
# project_names = [fn for fn in os.listdir(New_readfile_path) if ".java" in fn]  # fn 表示的是文件名
# print(project_names)

# table_dict = {}
# column_dict = {}
# wast_list=[]
column_line_id = []


def readlinesA(example_file, table_dict, column_dict, wast_list):
    with  open(New_readfile_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readlines = read_file.read()
        # print(readlines)

        spl = re.split(r'[\t|\n]', readlines)
        spl = [k for k in spl if k is not '']
        spl = "".join(spl)
        # table_dict
        splA, splB = spl.split("public class")
        description = ""
        name = re.compile("\/\*\*.*?\*/").findall(splA)
        # print(name)
        if name:
            name = re.compile("\w+").findall(name[0])
            name = " ".join(name)
            # print(name)

        tab = re.compile("\@Table.*?\)").findall(splA)
        if tab:
            tab = tab[0]
            tab = re.compile('\".*?\"').findall(splA)[0]
            tab = tab.split('"')[1]
            # print(tab)
            table_dict[tab] = name

        # column dict  带解释
        splBB = re.compile("\/\*\*.*?\;").findall(splB)
        # print(00,splBB)

        for colStr in splBB:
            wast = re.compile('private.*?\;').findall(colStr)
            wast_list.append(wast[0])
            if "name=" in colStr or "name =" in colStr:
                tab = re.compile('\".*?\"').findall(colStr)
                if '"TIMESTAMP"' in tab:
                    tab.remove('"TIMESTAMP"')
                tab = tab[0].split('"')
                tab.remove('')
                tab.remove('')
                # print(tab[0])
            else:
                if "@Column" in colStr:
                    tab = re.compile('\).*?private.*?\;').findall(colStr)
                    tab = tab[0].split(" ")[-1].split(";")[0].split(" ")
                    # print(tab, colStr)
                else:
                    tab = re.compile('private.*?\;').findall(colStr)
                    tab = tab[0].split(" ")[-1].split(";")

                #     tab="x"

                # print(tab[0])

            name = re.compile("\/\*\*.*?\*/").findall(colStr)
            name = re.compile("\w+").findall(name[0])
            name = " ".join(name)
            # print(name)
            column_dict[tab[0]] = name


def readlinesB(example_file, table_dict, column_dict, wast_list):
    with  open(New_readfile_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readlines = read_file.readlines()
        # print(readlines)
        for line in readlines:
            if "private" in line and ";" in line:
                # print(line)
                test = re.compile('private.*?\;').findall(line)
                if test[0] not in wast_list:
                    spl = line.split(";")
                    splA = spl[0]
                    splA = re.split(r'[\t|\n|//]', splA)

                    splA = splA[-1].split(" ")[-1]
                    # print(splA)

                    splB = spl[1]
                    splB = re.split(r'[\t|\n|\n|//]', splB)

                    description = "".join(splB)
                    if splA not in column_dict:
                        column_dict[splA] = description


def read_fileC(example_file, table_dict, column_dict, wast_list):
    with  open(New_readfile_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readin = read_file.read()
        spl = re.split(r'[\t|\n]', readin)
        spl = [k for k in spl if k is not '']
        spl = "".join(spl)

        spl = re.compile("^.*?public class").findall(spl)[0]
        # print(spl)
        des = re.compile("\/\*.*?\*/").findall(spl)
        for r in des:
            # print(r)
            res = re.compile(r'[\u4e00-\u9fa5|（|）|(|)|、]+').findall(r)
            res = list(filter(lambda x: x != " ", res))
            if len(res) > 0 and (
                    "表" in res[0] or "书" in res[0] or "证" in res[0] or "录" in res[0] or "券" in res[0] or "协议" in res[
                0] or "方案" in res[0] or "清单" in res[0] or "页" in res[0]):
                # print(res)
                table_dict[list(table_dict.keys())[0]] = res[0]

def read_fileD(example_file, table_dict, column_dict, wast_list):
    with  open(New_readfile_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readin = read_file.read()
        spl = re.split(r'[\t|\n]', readin)
        spl = [k for k in spl if k is not '']
        spl = "".join(spl)
        spl = re.compile("SafetyLifecycleModel").findall(spl)
        column_dict.update(BaseModel_dict())

        if spl:
            column_dict.update(SafetyLifecycleModel_dict())






def parasJavaCode(example_file):
    table_dict = {}
    column_dict = {}
    wast_list = []
    readlinesA(example_file, table_dict, column_dict, wast_list)
    readlinesB(example_file, table_dict, column_dict, wast_list)
    read_fileD(example_file, table_dict, column_dict, wast_list)

    if table_dict:
        read_fileC(example_file, table_dict, column_dict, wast_list)
    return table_dict, column_dict, wast_list


def writeInExcel(workbook, table_dict, column_dict, noNameId):
    if table_dict:
        worksheet = workbook.add_sheet(list(table_dict.keys())[0].upper())
        worksheet.write(0, 0, table_dict[list(table_dict.keys())[0]])
        worksheet.write(1, 0, list(table_dict.keys())[0])
    else:
        worksheet = workbook.add_sheet("noName" + str(noNameId))
        noNameId += 1

    for i, (k, v) in enumerate(column_dict.items()):
        worksheet.write(i + 1, 2, k)
        worksheet.write(i + 1, 3, v)
    return noNameId


def main():
    workbook = xlwt.Workbook()
    noNameId = 1

    project_names = [fn for fn in os.listdir(New_readfile_path) if ".java" in fn]  # fn 表示的是文件名
    # print(project_names)
    for filename in project_names:
        # try:
        table_dict, column_dict, wast_list = parasJavaCode(filename.upper())
        print(table_dict, column_dict)
        noNameId = writeInExcel(workbook, table_dict, column_dict, noNameId)
    workbook.save('yinjiwuzi.xls')

    # workbook.save('newModel.xls')


class NewModel():
    table = {}
    columns = {}
    tablename = ""

    def __init__(self, table, columns):
        self.table = table
        self.columns = columns
        # self.tablename=list(table.keys())[0]


def JavaGetNew():
    project_names = [fn for fn in os.listdir(New_readfile_path) if ".java" in fn]  # fn 表示的是文件名
    a = []
    for filename in project_names:
        # try:
        table_dict, column_dict, wast_list = parasJavaCode(filename)
        a.append(NewModel(table_dict, column_dict))
    return a


def SafetyLifecycleModel_dict():
    SafetyLifecycleModel = {"guid": "唯一值",
                            "createDate": "createDate",
                            "creator": "creator",
                            "lastChangedDate": "最后修改时间",
                            "lastChanger": "最后修改人",
                            "deleteFlag": "删除标志",
                            "systemVersion": "systemVersion"}
    return SafetyLifecycleModel


def BaseModel_dict():
    BaseModel = {
        "id": "",
        "version": "乐观锁控制字段"
    }

    return BaseModel


def test():
    example_file = "DocNewqzcxsqs.java"
    table_dict, column_dict, wast_list = parasJavaCode(example_file)
    print(table_dict, column_dict)



def readModelD(example_file, table_dict, column_dict, wast_list):
    with  open(New_readfile_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readlines = read_file.read()
        # print(readlines)

        spl = re.split(r'[\t|\n]', readlines)
        spl = [k for k in spl if k is not '']
        spl = "".join(spl)
        # table_dict
        split_table_colum=spl.split("public class")
        # print(split_table_colum)
        splA, splB =None,None
        if len(split_table_colum)<2:
            splA, splB=spl.split("public abstract class")
        else:
            splA, splB =split_table_colum
        print(splA)



def parasJavaCode2(example_file):
    table_dict = {}
    column_dict = {}
    wast_list = []
    readModelD(example_file, table_dict, column_dict, wast_list)


    if table_dict:
        read_fileC(example_file, table_dict, column_dict, wast_list)
    return table_dict, column_dict, wast_list

def main2():
    workbook = xlwt.Workbook()
    noNameId = 1

    project_names = [fn for fn in os.listdir(New_readfile_path) if ".java" in fn]  # fn 表示的是文件名
    # print(project_names)
    for filename in project_names:
        # try:
        table_dict, column_dict, wast_list = parasJavaCode2(filename.upper())
        # print(table_dict, column_dict)
        noNameId = writeInExcel(workbook, table_dict, column_dict, noNameId)
    workbook.save('yinjiwuzi.xls')


if __name__ == '__main__':
    # main()
    main2()
    # test()
    # print(JavaGetNew())
    # new_model=JavaGetNew()
    # for o_m in new_model:
    #     print(o_m.table)
