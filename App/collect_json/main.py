# imports
import os, json
from datetime import datetime

# variables


class CollectJson:
    count = -1
    extension = ".json"

    def __init__(self):
        pass

    def get_path(self):
        dir_list = os.listdir("min_json")
        file_path = "./min_json/" + dir_list[0]
        return file_path

    def read_min_json(self):
        path = self.get_path()
        with open(path, "r") as json_file:
            json_content = json.load(json_file)
        print(json_content)
        return json_content

    def del_file(self):
        os.remove(self.get_path())

    def new_file(self):
        date = datetime.now()
        date = date.strftime("%d-%m-%y")
        try:
            new_file = open(f"./day_json/{date}{self.extension}", "x")
            return new_file
        except FileExistsError:
            new_file = open(f"./day_json/{date}{self.extension}", "r")
            return


# main code
jsonc = CollectJson()
jsonc.new_file()
jsonc.read_min_json()
