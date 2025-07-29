import json

def accessValue(sampleJson, key = "key2"):

    data = json.loads(sampleJson)
    for key in data:
        if key == "key2":
            print(data[key])

sampleJson = """{"key1": "value1", "key2": "value2"}"""
accessValue(sampleJson)