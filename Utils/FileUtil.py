import os

base_path = "E:\VUEworkSPace\lnProject"
count = 0
project_names = [fn for fn in os.listdir(base_path) if "." not in fn]  # fn 表示的是文件名
print(project_names)

projects = {"cfInsProject": "赤峰",
            "ddInsProject": "丹东",
            "dljpProject": "大连金普",
            "hldCountyInsProject": "葫芦岛地级市",
            "hldInsProject": "葫芦岛",
            "lnProject": "辽宁",
            "neuProject": "东大",
            "occTestProject": "职业卫生",
            "pjInsProject": "盘锦",
            "sfxqInsProject": "沈抚新区",
            "syInsProject": "沈阳",
            "syPeaceInsProject": "康平",
            "syStudyProject": "沈阳学习",
            "txqInsProject": "沈阳铁西",
            "wjInsProject": "吴江",
            "ykInsProject": "营口",
            "jzInsProject": "锦州",
            "zhyProject": "中航油"}


def traves():
    for proj in project_names:
        path = base_path + os.sep + proj + os.sep + "src"
        print(path)

        for fn in os.listdir(path):
            if "." not in fn:
                print(fn)


def valid_file_exist(projects,filename):
    exceptions = []
    existions = []
    for proj in projects.keys():
        path = base_path + os.sep + proj + os.sep + "src" + os.sep + "views\\inspection\\caseApprovalConfig1\\rightVue"
        try:
            files = os.listdir(path)
            if filename in files:
                print(proj, files)
                existions.append(path)
        except:
            exceptions.append(proj)

    print("没有文件路径", exceptions)
    return existions

def copy_2_files(origin_path, origin_file_name, pathes):
    with open(origin_path + os.sep + origin_file_name, "r") as origin_file:
        # content = origin_file.read()
        for path in pathes:
            with open(path + os.sep + origin_file_name, "w") as copy2_file:
                # copy2_file.write(content)
                print(path + os.sep + origin_file_name)

destination_pathes=valid_file_exist(projects,'rightTable.vue',)
print(destination_pathes)

copy_2_files(destination_pathes[0],'rightTable.vue',destination_pathes)

