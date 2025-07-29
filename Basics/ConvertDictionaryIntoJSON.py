import json

def convertDictToJSON(data):

    data_json = json.dumps(data)

    return data_json


data = {"key1": "value1", "key2": "value2"}
print(convertDictToJSON(data))