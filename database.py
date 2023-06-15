import json

class DataBase:
    def edit(file_name, settings):
        with open(file_name, "wt", encoding="utf-8") as file:
            json.dump(settings, file, indent=2)

    def learn(file_name):
        with open(file_name, "rt", encoding="utf-8") as file:
            data = json.load(file)
            return data
