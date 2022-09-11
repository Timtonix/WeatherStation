import json, datetime, os

class CollectJson:

    def __init__(self):
        pass

    def get_date(self):
        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d-%m-%y")
        return date_now

    def get_timestamp(self):
        timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        return timestamp

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


    def process_weather_files(self, weather_data, day_weather, timestamp):
        day_weather["temp"][f"{timestamp}"] = weather_data["temp"]
        day_weather["humidity"][f"{timestamp}"] = weather_data["humidity"]
        return day_weather

    def write_in_the_day_file(self, modified_day_weather):
        with open(f"day_weather_json/{self.get_date()}.json", "w") as json_file:
            json.dump(modified_day_weather, json_file, indent=4)
        return modified_day_weather

    def main(self):
        timestamp = self.get_timestamp()
        weather_file = self.load_weather_file()
        day_weather_file = self.load_day_weather_file()
        process = self.process_weather_files(weather_file, day_weather_file, timestamp)
        return self.write_in_the_day_file(process)
