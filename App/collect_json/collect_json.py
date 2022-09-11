# imports
import os
import json
import pytz
from datetime import datetime


# variables


class CollectJson:
    count = -1
    extension = ".json"

    def __init__(self):
        pass

    def get_min_path(self):
        dir_list = os.listdir("min_json")
        file_path = "./min_json/" + dir_list[0]
        return file_path

    def read_min_json(self):
        path = self.get_min_path()
        with open(path, "r") as json_file:
            json_content = json.load(json_file)
        return json_content

    def read_day_json(self):
        day_json = self.open_day_json()
        json_content = json.load(day_json)
        return json_content

    def open_day_json(self):
        date = self.get_date()
        try:
            new_file = open(f"./day_json/{date}{self.extension}", "x")
            return new_file
        except FileExistsError:
            new_file = open(f"./day_json/{date}{self.extension}", "r+")
            return new_file

    def get_date(self):
        date = datetime.now(tz=pytz.timezone('Europe/Paris'))
        date = date.strftime("%d-%m-%y")
        return date

    def get_timestamp(self):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        return timestamp


    def write_in_day_file(self):
        min_json = self.read_min_json()
        day_json = self.read_day_json()
        temp_min = min_json['temp']
        humidity_min = min_json['humidity']
        new_key = {"temp": {f"{self.get_timestamp()}": temp_min}}
        with open(f"./day_json/{self.get_date()}{self.extension}", "w") as jsonFile:
            json.dump(new_key, jsonFile, indent=4)





# main code
jsonc = CollectJson()
jsonc.open_day_json()
jsonc.write_in_day_file()
