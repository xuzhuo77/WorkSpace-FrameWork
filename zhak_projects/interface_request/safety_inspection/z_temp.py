from zhak_projects.interface_request import yaml_io

path_filename = "E:\pythonWebWorkSpace\zhak_projects\interface_request\safety_inspection\z_temp.yaml"


def write_default(data={}):
    yaml_io.write_default(path_filename, data)


def read_default():
    return yaml_io.read_default(path_filename)
