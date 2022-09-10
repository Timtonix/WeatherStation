# imports
import json
import os


# functions
def get_path():
    dir_list = os.listdir("./min_json")
    file_path = dir_list[1]
    return file_path


def read_json():
    path = "./min_json/" + get_path()
    with open(path) as json_file:
        json_content = json_file.read()
        with open("./day_json", "x") as newfile:
            newfile.write(json_content)


# main code
read_json()
