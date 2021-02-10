

import yaml

def read_default(path_name):
    with open(path_name, "r") as rf:
        content = yaml.load(rf.read(), Loader=yaml.FullLoader)
        return content


def write_default(path_name,data={}):
    with open(path_name, "r") as rf:
        content = yaml.load(rf.read(), Loader=yaml.FullLoader)
        # [for d in data]
        content.update(data)
        with  open("access_file.yaml", "w") as wf:
            yaml_obj = yaml.dump(content, wf)