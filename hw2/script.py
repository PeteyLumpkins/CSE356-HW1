from pymongo import MongoClient
import os
import json

if __name__ == "__main__":
    
    connection = "localhost:27017"
    database = "hw2"
    collection = "63045addfc20c72c72f3c18f"

    client = MongoClient(connection)
    data = []
    
    # This will clean out all the docs in the collection - we don't want to have duplicates
    client[database][collection].delete_many({})

    for item in os.listdir():
        if(os.path.isdir(item)):
            for file in os.listdir(item):
                
                if (file.endswith(".json")):
                    with open(item + "/" + file, "r") as f:
                        data.append(f.read())

    
    json_data = []
    for i in range(0, len(data)):
        json_data.append(json.loads(data[i]))

    client[database][collection].insert_many(json_data)
#   [print(doc) for doc in client[database][collection].find({})]
