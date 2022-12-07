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

    def create_day_weather_file(self):  # Cette fonction renvoie True si le fichier vient d'être crée ou False si le fichier existe déjà
        directory = os.listdir('day_weather_json/')
        date = f"{self.get_date()}.json"
        if date in directory:
            return False  # Comme le fichier existe déjà on renvoie false
        else: # Si le fichier est vide alors on le crée et on met la template de base -> {"temp": {"timestamp": False}, "humidity": {"timestamp": False}}
            #Cela permet au code de comprendre comment est structuré le json
            with open(f"day_weather_json/{self.get_date()}.json", "x") as weather_day_file:
                json.dump({"temp": {"timestamp": False}, "humidity": {"timestamp": False}, "rain": {"timestamp": False}}, weather_day_file, indent=4)
                return True  # On a finit de crée le fichier donc on renvoie true

    def load_day_weather_file(self):
        self.create_day_weather_file()
        with open(f"day_weather_json/{self.get_date()}.json", "r") as json_file:
            json_content = json.loads(json_file.read())
            return json_content

    def process_weather_files(self, weather_data_sensor, day_weather_file, timestamp):
        day_weather_file["temp"][f"{timestamp}"] = weather_data_sensor["temp"]
        day_weather_file["humidity"][f"{timestamp}"] = weather_data_sensor["humidity"]
        day_weather_file["rain"][f"{timestamp}"] = weather_data_sensor["rain"]
        return day_weather_file

    def write_in_the_day_file(self, modified_day_weather):
        with open(f"day_weather_json/{self.get_date()}.json", "w") as json_file:
            json.dump(modified_day_weather, json_file, indent=4)
        return modified_day_weather

    def main(self, weather_data_sensor):
        timestamp = self.get_timestamp()
        if self.create_day_weather_file():
            day_weather_file = self.load_day_weather_file()
        else:
            day_weather_file = self.load_day_weather_file()
        process = self.process_weather_files(weather_data_sensor, day_weather_file, timestamp)
        return self.write_in_the_day_file(process)
