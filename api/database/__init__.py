from fastapi import FastAPI
from database import MongoDb


def setup_curd(app: FastAPI):
    app.add_api_route('/curd', endpoint=MongoDb.search, methods=["GET"])
    app.add_api_route('/curd', endpoint=MongoDb.update_record, methods=["PATCH"])
    app.add_api_route('/curd', endpoint=MongoDb.delete_record, methods=["DELETE"])
    app.add_api_route('/curd', endpoint=MongoDb.create_record, methods=["POST", "PUT"])
