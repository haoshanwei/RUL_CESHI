import json

# fp = open("../test_data/login.json")
# data = json.load(fp)
# print(data)

# print("-------这又是一次伟大的转折------------")

class operationJson(object):
    def __init__(self, file_path="../test_data/login.json"):
        self.file_path = file_path
        self.data = self.get_data()

    def get_data(self):
        with open(self.file_path) as f:
            data = json.load(f)
            return data

    def get_key_value(self, key=None):
        if key:
            return self.data[key ]
        else:
            return self.data


# print(operationJson().get_key_value("name"))