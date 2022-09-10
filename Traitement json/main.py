# imports
import os


# functions
def get_path():
    dir_list = os.listdir("./min_json")
    file_path = dir_list[1]
    return file_path


def read_json():
    path = "./min_json/" + get_path()
    with open(path, "r") as json_file:
        json_content = json_file.read()
    return json_content


# main code
