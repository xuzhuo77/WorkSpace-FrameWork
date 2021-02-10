import os
import re

old_model_files_path = "C:\\Users\\Administrator\\Desktop\\同步库\\old_model"

project_names = [fn for fn in os.listdir(old_model_files_path) if ".java" in fn]  # fn 表示的是文件名
print(project_names)

example_file = 'zjkCity_Menu.java'
example_file = 'Z_DocXzjcjgbg.java'

table_dict = {}
column_dict = {}

column_line_id = []


def file_readA(example_file, table_dict, column_dict, wast_list):
    with  open(old_model_files_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readin = read_file.read()
        spl = readin

        des = re.compile("\@ModelDescriptor.*").findall(spl)
        tab = re.compile("\@Table.*").findall(spl)
        # print(des[0].split("moduleNameCn = ")[-1].split('"')[1] , tab[0].split("name = ")[-1].split('"')[1])
        tabk = tab[0].split("name = ")[-1].split('"')[1]
        desv = ""
        if des:
            desv = des[0].split("moduleNameCn = ")[-1].split('"')[1]

        table_dict[tabk] = desv
        spl = re.split(r'[\t|\n]', readin)
        spl = [k for k in spl if k is not '']

        spl = "".join(spl)

        # print(spl)

        spl = re.compile("\@FieldDescriptor.*?\;").findall(spl)

        for k in spl:
            column = re.compile("private.*?\;").findall(k)
            discription = re.compile('label = ".*?\"').findall(k)
            column_dict[column[0].split(" ")[-1][0:-1]] = discription[0].split('"')[1]

        # print(table_dict)
        # print("column",column_dict)

        spl2 = readin
        spl2 = re.compile("private .*?\;").findall(spl2)
        # print(spl2,12312)

        # private Integer xxxx;  准备
        for k in spl2:
            column_line_id.append(k)
            if k.split(" ")[2][0:-1] not in column_dict.keys():
                column_dict[k.split(" ")[2][0:-1]] = ""
            else:
                # print(k.split(" ")[2][0:-1], 2)
                if column_dict[k.split(" ")[2][0:-1]] is "":
                    pass


def file_readB(example_file, table_dict, column_dict, wast_list):
    with  open(old_model_files_path + os.sep + example_file, "r", encoding="utf") as read_file:
        readlines = read_file.readlines()
        # print(readlines)

        for line in readlines:
            for clo in column_line_id:
                if clo in line:
                    line = line.split('\n')[0]
                    # print(line)
                    splinS = line.split(";")
                    if len(splinS)>2:
                        splinS=[splinS[0],";".join(splinS[1:])]

                    splinA, splinB=splinS
                    splinB=splinB.split("//")
                    description=""
                    if len(splinB)>1:
                        description=splinB[1]

                    if "=" in splinA:
                        spline=list(filter(lambda x: x!="",splinA.split("=")[0].split(" ")))[-1]
                        # print(spline)
                        column_dict[spline] = description
                    else:
                        if column_dict[splinA.split(" ")[-1]] is '':
                            column_dict[splinA.split(" ")[-1]] = description

                    #
                    #
                    # # print(splin[0].split(" ")[-1][0:-1])
                    # description = ""
                    # if len(splin) > 1:
                    #     description = splin[-1]
                    # # print(column_dict[splin[0].split(" ")[-1][0:-1]])
                    # if "=" in splin[0]:
                    #     spline=list(filter(lambda x: x!="",splin[0].split("=")[0].split(" ")))[-1]
                    #     print(spline)
                    #     column_dict[spline] = description
                    #
                    #
                    # else:
                    #     # print(splin[0].split(" ")[-1][0:-1])
                    #     if column_dict[splin[0].split(" ")[-1][0:-1]] is '':
                    #         column_dict[splin[0].split(" ")[-1][0:-1]] = description

def read_fileC(example_file, table_dict, column_dict, wast_list):
    with  open(old_model_files_path + os.sep + example_file, "r", encoding="utf") as read_file:
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
            res=list(filter(lambda x :x!=" ",res))
            if len(res)>0 and ("表" in res[0] or "书" in res[0] or "证" in res[0] or "录" in res[0] or "券" in res[0] or "协议" in res[0] or "方案" in res[0] or "清单" in res[0] or"页" in res[0]):
                table_dict[list(table_dict.keys())[0]]=res[0]



def oldread():
    file_readA(example_file)
    file_readB(example_file)
    print(column_dict)


def parasJavaCode(example_file):
    table_dict = {}
    column_dict = {}
    wast_list = []
    file_readA(example_file, table_dict, column_dict, wast_list)
    file_readB(example_file, table_dict, column_dict, wast_list)

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


import xlwt


def main():
    workbook = xlwt.Workbook()
    noNameId = 1

    project_names = [fn for fn in os.listdir(old_model_files_path) if ".java" in fn]  # fn 表示的是文件名
    # print(project_names)
    for filename in project_names:
        print("[[[[{}]]]]".format(filename))
        # try:
        table_dict, column_dict, wast_list = parasJavaCode(filename.upper())
        print(table_dict, column_dict)
        noNameId = writeInExcel(workbook, table_dict, column_dict, noNameId)

    workbook.save('oldModel.xls')


def test():
    example_file = "Z_DocNewXzqzxcbl.java"
    table_dict, column_dict, wast_list = parasJavaCode(example_file)
    print(table_dict, column_dict)

class OldModel():
    table={}
    columns={}
    tablename=""
    def __init__(self,table,columns):
        self.table=table
        self.columns=columns
        self.tablename=list(table.keys())[0]
def JavaGetOld():
    project_names = [fn for fn in os.listdir(old_model_files_path) if ".java" in fn]  # fn 表示的是文件名
    a=[]
    for filename in project_names:
        # try:
            table_dict,column_dict,wast_list=parasJavaCode(filename)
            a.append(OldModel(table_dict,column_dict))
    return a


if __name__ == '__main__':
    main()
    # test()
    # old_model=JavaGetOld()
    # for o_m in old_model:
    #     print(o_m.table)
