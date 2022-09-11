import json, datetime, os

class CollectJson:

    def __init__(self):
        pass

    def get_date(self):
        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d-%m-%y")
        return date_now

    def create_day_weather_file(self):
        dir = os.listdir('./day_weather_json')
        date = f"{self.get_date()}.json"
        if date in dir:
            return False
        else:
            with open(f"./day_weather_json/{self.get_date()}.json", "x") as weather_day_file:
                json.dump({}, weather_day_file, indent=4)
                return True


    def load_weather_file(self):
        with open("weather_json/data.json", "r") as json_data:
            json_content = json.load(json_data)
        return json_content

    def load_day_weather_file(self):
        created = self.create_day_weather_file()
        with open(f"./day_weather_json/{self.get_date()}.json", "r") as json_file:
            json_content = json.loads(json_file.read())
            return json_content

