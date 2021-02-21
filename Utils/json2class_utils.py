import json

test = {"name": "Abc", "age": "12"}
test2 = {"name": "Abc", "age": "12"}
dict = {"personLook": test}
person_list={"items":[test,test]}


def class_dict2class(_dict,class_name):
    if len(_dict.keys()) > 1:
        raise ValueError("not a class")

    if not class_name:
        class_name = list(_dict.keys())[0]
    attributes = []

    for key in _dict[class_name].keys():
        attributes.append("\t" + str(key)[0].lower() + str(key)[1:] + "= None")

    clazz = ["class ",
             class_name[0].upper() + class_name[1:],
             "():",
             "\n" + "\n".join(attributes)
             ]

    return " ".join(clazz), class_name


def class_dictlist2class(_dict,class_name):

    if not class_name:
        class_name = list(_dict.keys())[0]

    key = list(_dict.keys())[0]

    if not isinstance(_dict[key],list):
        raise ValueError("not list")
    items=_dict[key]

    return class_dict2class({class_name:items[0]},class_name)


print()


def file_get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()




# clazz, class_name = class_dict2class(dict)
clazz, class_name=class_dictlist2class(person_list,"PersonRun")
with open(file_get_lower_case_name(class_name) + ".py", "w") as f:
    f.write("# coding:utf-8\n")
    f.write(clazz)
