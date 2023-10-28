from pymongo import MongoClient, DESCENDING
from pymongo.errors import ServerSelectionTimeoutError
from threading import Lock
from config import db_string, db, collection
from fastapi import Query,  Body
from fastapi.responses import JSONResponse


class MongoDb:
    def __init__(self):
        self.client = MongoClient(db_string)
        self.db = self.client[db]
        self.lock = Lock()

    async def search(self, field_name: str = Query(..., title="Field Name",
                                                   description="Vame of field using which field is identified"),
                     field_value: str or int or dict = Query(..., title="Field Value",
                                                             description="Value of field using which field is identified")):
        """
        using method get
        search items with the specified field, value and return one value or all values as specified
        :return:
        """
        try:
            # if attrs.find__all():
            #     data = self.db[collection].find({attrs.field_name: attrs.field_value})
            # else:
            data = self.db[collection].find_one({field_name: field_value})
            try:
                del data['_id']
            except (KeyError, TypeError):
                pass
            return data
        except ServerSelectionTimeoutError:
            return JSONResponse({"error": "server not found"}, status_code=500)

    async def search_post(self, field_name: str = Query(..., title="Field Name",
                                                        description="Vame of field using which field is identified"),
                          field_value: str or int or dict = Query(..., title="Field Value",
                                                                  description="Value of field using which field is identified"),
                          find_all: bool or None = Query(False, title="Find All",
                                                         description="Find all records or just one")):
        """
        using method get
        search items with the specified field, value and return one value or all values as specified
        :return:
        """
        if find_all:
            data = self.db[collection].find({field_name: field_value})
        else:
            data = self.db[collection].find_one({field_name: field_value})
        try:
            del data['_id']
        except (KeyError, TypeError):
            pass
        return data

    async def create_record(self, data: dict = Body(...)):
        """
        using method post
        adds the data to the specified collection or default collection
        :return:
        """
        print(data)
        print(type(data))
        with self.lock:
            return {"item_id": str(self.db[collection].insert_one(data).inserted_id)}

    async def delete_record(self, field_name: str = Body(..., title="Field Name",
                                                         description="Name of field using which field is identified"),
                            field_value: str or int or dict = Body(..., title="Field Value",
                                                                   description="Value of field using which field is identified")):
        """
        using method delete
        delets a record which matches the parms passed
        :param field_name: Name of the field which is used to identify the record
        :param field_value: Value of the field which is used to identify the record
        :return:
        """
        with self.lock:

            data = self.db[collection].find_one_and_delete(
                {field_name: field_value},
                sort=[('_id', DESCENDING)]
            )
            print(data)
            try:
                del data['_id']
            except (KeyError, TypeError):
                pass
            return data

    async def update_record(self, field_name: str = Body(..., title="Field Name",
                                                         description="Name of field using which field is identified"),
                            field_value: str or int or dict = Body(..., title="Field Value",
                                                                   description="Value of field using which field is identified"),
                            data: dict = Body(..., title="Data", description="Data to be updated")):
        """"
        using method put
        updates a record which matches the parms passed
        :return:
        """
        data = self.db[collection].find_one_and_update({field_name: field_value}, {'$set': data})
        try:
            del data['_id']
        except (KeyError, TypeError):
            pass
        with self.lock:
            return {
                "old value": data
            }


MongoDb = MongoDb()
