from docx import Document
import xlrd

from zhak_projects.databases_connection import DB_startover

path = "C:\\Users\\Administrator\\Desktop\\应急管理物资\\"
file = path + "物资类型.xls"

workbook = xlrd.open_workbook(file)  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。

table = workbook.sheet_by_index(0)
codes = table.col_values(6, start_rowx=0, end_rowx=None)

table_list = {}
print(type(codes))

for i in range(table.nrows):
    row = table.row_values(i)
    row[6] = str(row[6]).strip()
    table_list[row[6]] = row


# print(table_list)
def parse(str):
    if "." in str:
        return str[0:2], str[2], str[3:5], str[6], str[7:]


print(parse("43D16.A16"))
table_list.pop("code")
table_list2 = {}
for k, v in table_list.items():
    code = parse(v[6])
    if code is not None:
        parent = None
        if code[4] != "00":
            parent_code = code[0] + code[1] + code[2] + "." + code[3] + "00"

            parent_id = table_list[parent_code][0]
            parent_name = table_list[parent_code][7]
            table_list[parent_code][5] = 0
            v[3] = parent_id
            v[4] = parent_name

        elif code[4] == "00":
            if code[3] != "0":
                parent_code = code[0] + code[1] + code[2] + "." + "0" + "00"
                parent_id = table_list[parent_code][0]
                parent_name = table_list[parent_code][7]
                table_list[parent_code][5] = 0
                v[3] = parent_id
                v[4] = parent_name

            elif code[3] == "0":
                if code[2] != "00":
                    parent_code = code[0] + code[1] + "00" + "." + "0" + "00"
                    parent_id = table_list[parent_code][0]
                    parent_name = table_list[parent_code][7]
                    table_list[parent_code][5] = 0
                    v[3] = parent_id
                    v[4] = parent_name

                elif code[2] == "00":
                    v[3] = -1.0
                    v[5] = 0
for v in table_list.items():
    print(v)
# print(len(table_list))
from sqlalchemy import Column, String, create_engine, Integer, TIMESTAMP, FLOAT, BOOLEAN, CHAR, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class SuppliesCatagory(BaseModel):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "T_SUPPLIES_CATAGORY"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    id = Column(primary_key=True)  # Column类创建一个字段
    version = Column()
    sort_id = Column()
    parent_id = Column()  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    parent_name = Column()
    leaf = Column()
    code = Column()
    name = Column()
    remark = Column()


# DB_startover.delete(SuppliesCatagory)


def main():
    global table
    a = SuppliesCatagory.__table__.insert()
    print(a)
    data = table_list["43C00.000"]
    keys = ['id', 'version', 'sort_id', 'parent_id', 'parent_name', 'leaf', 'code', 'name', 'remark']
    print(data)
    table = 'T_SUPPLIES_CATAGORY'
    value = [dict(zip(keys, v)) for v in table_list.values()]
    print(value)
    DB_startover.execute_sql(sql=SuppliesCatagory.__table__.insert(), value=value)
    # insert(['43', 'D', '16', 'A', '16'])


def some_guids():
    return ('b6884bf4-7453-4e9a-8fb4-d85b8b403c06',
            '6a7c872f-f523-4824-a60c-70a21444b051',
            '4ca1949a-03db-498e-bb95-0aa9d334703a',
            '04a9c0b6-1bc3-469d-a693-380f132a74c9',
            '257dc2c9-af87-4e7f-9357-40831f63c2d8',
            '91e106d2-85ab-4e4e-b601-b8a1525c2e53',
            'b5c3ca3a-e497-463d-8fd1-838d5aef388b',
            '89d5557b-9bb9-41d4-a964-aaed1fd38fbc',
            'da988910-1574-4d8d-ae54-f32079fe3df1',
            '60aeec39-b7b2-4586-9488-a90652beae21',
            '929e7c79-91fb-4fa6-afab-5891201a6088',
            '683c2d50-dd1d-489c-a996-1f6ee57a4a03',
            '3d894439-d01b-41c9-9405-8571f9b1e703',
            'f380379e-5ea7-409d-aae6-c3d3cb45ef73')


if __name__ == '__main__':
    main()
