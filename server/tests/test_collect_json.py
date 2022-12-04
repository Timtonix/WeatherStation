import os
import json
import datetime
from server import collect_json

collect_json = collect_json.CollectJson()


class TestCollectJson:

    def test_load_day_weather_file(self):
        json = collect_json.load_day_weather_file()
        assert type(json) is dict

    def test_get_date(self):
        date = collect_json.get_date()
        true_date = datetime.datetime.now()
        true_date = true_date.strftime("%d-%m-%y")
        assert date == true_date

    def test_create_day_weather_file(self):
        json_file = collect_json.create_day_weather_file()
        dir = os.listdir('../day_weather_json')
        date = f"{collect_json.get_date()}.json"
        if date in dir:
            assert True
        else:
            assert False

    def test_process_weather_files(self):
        timestamp = collect_json.get_timestamp()
        weather_data = {"temp": 30, "humidity": 156}
        day_weather = {"temp": {"today": 26}, "humidity": {"today": 164}}
        process = collect_json.process_weather_files(weather_data, day_weather, timestamp)
        modified_day_weather = {"temp": {f"{timestamp}": 30, "today": 26}, "humidity": {f"{timestamp}": 156, "today": 164}}
        assert modified_day_weather == process

    def test_write_in_the_day_file(self):
        timestamp = collect_json.get_timestamp()
        modified_day_weather = {"temp": {f"{timestamp}": 30, "today": 26}, "humidity": {f"{timestamp}": 156, "today": 164}}
        collect_json.write_in_the_day_file(modified_day_weather)
        with open(f"day_weather_json/{collect_json.get_date()}.json", "r") as json_file:
            json_content = json.loads(json_file.read())
            assert json_content == modified_day_weather

    def test_main(self):
        writed = collect_json.main({"temp": 23, "humidity": 154})
        with open(f"day_weather_json/{collect_json.get_date()}.json", "r") as json_file:
            json_content = json.loads(json_file.read())
        assert writed == json_content
