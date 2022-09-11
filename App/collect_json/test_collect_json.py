import pytest
import os
import json
import datetime
import collect_json

collect_json = collect_json.CollectJson()

class TestCollectJson:
    def test_load_weather_file(self):
        json = collect_json.load_weather_file()
        assert type(json) is dict

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
        dir = os.listdir('./day_weather_json')
        date = f"{collect_json.get_date()}.json"
        if date in dir:
            assert True
        else:
            assert False


