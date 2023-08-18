from fastapi import FastAPI
from database import MongoDb


def setup_database_post_only_routes(app: FastAPI):
    app.add_api_route('/search', endpoint=MongoDb.search_post, methods=["POST"])
    app.add_api_route('/update', endpoint=MongoDb.update_record, methods=["POST"])
    app.add_api_route('/delete', endpoint=MongoDb.delete_record, methods=["POST"])
    app.add_api_route('/create', endpoint=MongoDb.create_record, methods=["POST"])
