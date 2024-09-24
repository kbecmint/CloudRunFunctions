import pymongo
import os
from datetime import datetime, date
import json

import requests

CONNECTION = os.environ.get("CONNECTION")

connection = CONNECTION


def record(place: str, todo: str):
    client = pymongo.MongoClient(connection)
    db = client["memo"]
    col = db["todo"]
    query = [
        {
            "place": place,
            "todo": todo,
            "created_at": datetime.now(),
        }
    ]
    col.insert_many(query)
    client.close()


def getToDo(count: int = 200):
    with pymongo.MongoClient(connection) as client:
        db = client["memo"]
        col = db["todo"]
        ds = col.find(
            projection={"place": 1, "todo": 1, "created_at": 1, "_id": 0},
            sort=[("created_at", 1)],
        ).limit(count)
        ls = list(ds)
        return ls


def json_serial(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {obj} not serializable")


if __name__ == "__main__":

    ls = getToDo()
    json_string = json.dumps(ls, ensure_ascii=False, default=json_serial)

    headers = requests.get("http://127.0.0.1:8090/").headers
    print(headers)
