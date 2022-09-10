# imports
import os, main

# variables
count = -1
extension = ".json"

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


def del_file():
    os.remove(get_path())


def new_file():
    main.count += 1
    name = f"day_{main.count}_all_captors_file"
    path = "./day_json/" + name + main.extension
    print(path)


# main code
