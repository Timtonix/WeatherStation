# imports
import os


# functions
def get_path():
    dir_list = os.listdir("./min_json")
    file_path = dir_list[1]
    return file_path
