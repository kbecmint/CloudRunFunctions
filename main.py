import functions_framework
import flask
import mongo
from flask import jsonify, Response
import json

from datetime import date, datetime


def json_serial(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {obj} not serializable")


@functions_framework.http
def todo(request: flask.Request):
    method = request.method
    contentType = request.content_type

    if method == "GET":
        works = mongo.getToDo()
        return Response(
            json.dumps(works, ensure_ascii=False, default=json_serial),
            mimetype="application/json",
        )

    if method == "POST" and contentType == "application/json":
        data = request.get_json()
        print(data)
        print(f"{data['place']}:{data['todo']}")
        # mongo.record(w["place"], w["todo"])
        return Response(
            json.dumps(data, ensure_ascii=False, default=json_serial),
            mimetype="application/json",
        )

    return jsonify({"message": f" {method} Method Not Allowed"}), 405
