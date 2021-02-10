
import yaml


def read_default(file_name):
    with open(file_name,"r") as rf:
        content = yaml.load( rf.read(),Loader=yaml.FullLoader)
        return content

def write_default(file_name,data={}):
    with open(file_name,"r") as rf:
        content = yaml.load( rf.read(),Loader=yaml.FullLoader)
        # [for d in data]
        if not content:
            content={}
        content.update(data)
        with  open(file_name,"w") as wf:
            yaml_obj = yaml.dump(content, wf)