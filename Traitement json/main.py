# imports
import os, datetime

# functions
def get_path():
    dir_list = os.listdir("./min_json")
    file_path = "./min_json/" + dir_list[0]
    return file_path


def read_json():
    path = get_path()
    with open(path, "r") as json_file:
        json_content = json_file.read()
    return json_content


def del_file(file_path):
    os.remove(file_path)

# main code
