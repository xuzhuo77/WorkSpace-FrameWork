

# 导入tkinter模块

import tkinter
from tkinter import messagebox
import copy
from tkinter import *
import os

from zhak_projects.synchronation.tableNameService import getColumnsFromSql1,getColumnsFromSql2


from tkinter import ttk
import sys


sys.path.append("..")
global newTableColumns
global oldTableColumns
global mapping_columns
newTableColumns=[]
oldTableColumns=[]
mapping_columns=[]


def delButton(tree):
    items = tree.get_children()
    [tree.delete(item) for item in items]


def upatetableColumns(tree,columns):
    delButton(tree)
    for k,v in enumerate(columns):
        tree.insert("",k,values=v)

def load_columns_from_table1():
    base_path = E0.get()
    sql="select column_name from user_tab_columns   where Table_Name='{}'".format(base_path)
    result =getColumnsFromSql1(sql)
    global newTableColumns
    newTableColumns=[]
    for k, v in enumerate(result):
        newTableColumns.append((k,v[0].strip('\''),))
    upatetableColumns(tree0,newTableColumns)


def load_columns_from_table3():
    base_path = E4.get()
    sql="select column_name from user_tab_columns   where Table_Name='{}'".format(base_path)
    result =getColumnsFromSql2(sql)
    global oldTableColumns
    oldTableColumns=[]
    for k, v in enumerate(result):
        oldTableColumns.append((k,v[0].strip('\''),))
    upatetableColumns(tree4,oldTableColumns)

def mapping_new_old():
    global newTableColumns
    global oldTableColumns
    global mapping_columns
    mapping_columns=[]
    length=len(oldTableColumns) if len(oldTableColumns) <len(newTableColumns) else  len(newTableColumns)
    for i in range(length):
        mapping_columns.append((i,oldTableColumns[i][1],newTableColumns[i][1]))
    upatetableColumns(tree2,mapping_columns)

def treeviewClick0(event):  # 单击
    global newTableColumns
    global oldTableColumns
    global mapping_columns
    for item in tree0.selection():
        item_text = tree0.item(item, "value")
    item_text=None
    for item in  tree0.selection():
        item_text = tree0.item(item, "value")
    if item_text is not None:
        idx=None
        for i,v in enumerate(newTableColumns):
            if int(item_text[0]) == v[0]:
                idx=i
        a=newTableColumns.pop(idx)
        newTableColumns.insert(0,a)
        upatetableColumns(tree0,newTableColumns)

def treeviewClick4(event):  # 单击
    global newTableColumns
    global oldTableColumns
    global mapping_columns
    item_text=None
    for item in  tree4.selection():
        item_text = tree4.item(item, "value")
    if item_text is not None:
        idx=None
        for i,v in enumerate(oldTableColumns):
            if int(item_text[0]) == v[0]:
                idx=i
        a=oldTableColumns.pop(idx)
        oldTableColumns.insert(0,a)
        upatetableColumns(tree4,oldTableColumns)

# 创建主窗口对象
root = tkinter.Tk()
# root.geometry("300x200+10+20")
root.minsize(1200, 800)

f0 = tkinter.Frame(root)
f01 = tkinter.Frame(f0)
f01.grid(row=0,column=0)

f0.grid(row=0, column=0)
l0 = Label(f01,text="新表名")
l0.grid(row=0, column=0)

E0 = Entry(f01, bd=1, )
E0.grid(row=1, column=0)
E0.insert(END, "Z_DOC")

l0 = Label(f01,text="新表列名")
l0.grid(row=2, column=0)
b0 = Button(f01, width=12, text='载入库', command=load_columns_from_table1)
b0.grid(row=2, column=1)

tree0 = ttk.Treeview(f0,h=30)
tree0.grid(row=3, column=0)

tree0["columns"] = ("ID","列名", "解释", )     # #定义列
tree0.column("#0",minwidth=0,width=20, stretch=NO)
tree0.column("ID", width=120)          # #设置列
tree0.column("列名", width=120)          # #设置列
tree0.column("解释", width=120)
tree0.heading("列名", text="列名")        # #设置显示的表头名
tree0.heading("解释", text="解释")


tree0.bind('<ButtonRelease-1>', treeviewClick0)  # 绑定单击离开事件===========

# root.minsize(1200, 500)
f2 = tkinter.Frame(root)
f21 = tkinter.Frame(f2)
f21.grid(row=0,column=0)

f2.grid(row=0, column=4)
l2 = Label(f21,text="新旧对应")
l2.grid(row=0, column=0)

E2 = Entry(f21, bd=1, )
E2.grid(row=1, column=0)
E2.insert(END, "Z_DOC")

l2 = Label(f21,text="新旧列名")
l2.grid(row=2, column=0)
b2 = Button(f21, width=12, text='对齐', command=mapping_new_old)
b2.grid(row=2, column=1)

tree2 = ttk.Treeview(f2,h=30)
tree2.grid(row=3, column=0)
tree2["columns"] = ("id","old列", "new列", )     # #定义列
tree2.column("#0",minwidth=0,width=20, stretch=NO)
tree2.column("id", width=120)          # #设置列
tree2.column("old列", width=120)          # #设置列
tree2.column("new列", width=120)
tree2.heading("old列", text="old列")        # #设置显示的表头名
tree2.heading("new列", text="new列")



f4 = tkinter.Frame(root)
f41 = tkinter.Frame(f4)
f41.grid(row=0,column=0)

f4.grid(row=0, column=2)
l4 = Label(f41,text="旧表名")
l4.grid(row=0, column=0)

E4 = Entry(f41, bd=1, )
E4.grid(row=1, column=0)
E4.insert(END, "Z_DOC")

l4 = Label(f41,text="旧表列名")
l4.grid(row=2, column=0)
b4 = Button(f41, width=12, text='载入库', command=load_columns_from_table3)
b4.grid(row=2, column=1)

tree4 = ttk.Treeview(f4,h=30)
tree4.grid(row=3, column=0)
tree4["columns"] = ("ID","列名", "解释", )     # #定义列
tree4.column("#0",minwidth=0,width=20, stretch=NO)
tree4.column("ID", width=120)          # #设置列
tree4.column("列名", width=120)          # #设置列
tree4.column("解释", width=120)
tree4.heading("列名", text="列名")        # #设置显示的表头名
tree4.heading("解释", text="解释")
tree4.bind('<ButtonRelease-1>', treeviewClick4)  # 绑定单击离开事件===========



# 加入消息循环
root.mainloop()
