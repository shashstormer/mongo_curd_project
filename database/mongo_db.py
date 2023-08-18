from pymongo import MongoClient, DESCENDING
from threading import Lock
from models import Validatiors
from config import db_string, db, collection
from fastapi import Depends


class MongoDb:
    def __init__(self):
        self.client = MongoClient(db_string)
        self.db = self.client[db]
        self.lock = Lock()

    async def search(self, attrs: Validatiors.search = Depends()):
        """
        using method get
        search items with the specified field, value and return one value or all values as specified
        :param attrs:
        :return:
        """
        if attrs.find__all():
            data = self.db[collection].find({attrs.field_name: attrs.field_value})
        else:
            data = self.db[collection].find_one({attrs.field_name: attrs.field_value})
        try:
            del data['_id']
        except (KeyError, TypeError):
            pass
        return data

    async def search_post(self, attrs: Validatiors.search):
        """
        using method get
        search items with the specified field, value and return one value or all values as specified
        :param attrs:
        :return:
        """
        if attrs.find__all():
            data = self.db[collection].find({attrs.field_name: attrs.field_value})
        else:
            data = self.db[collection].find_one({attrs.field_name: attrs.field_value})
        try:
            del data['_id']
        except (KeyError, TypeError):
            pass
        return data

    async def create_record(self, attrs: Validatiors.create):
        """
        using method post
        adds the data to the specified collection or default collection
        :return:
        """
        print(attrs)
        print(attrs.data)
        print(type(attrs.data))
        with self.lock:
            return {"item_id": str(self.db[collection].insert_one(attrs.data).inserted_id)}

    async def delete_record(self, attrs: Validatiors.delete):
        """
        using method delete
        delets a record which matches the parms passed
        :param attrs:
        :return:
        """
        with self.lock:

            data = self.db[collection].find_one_and_delete(
                {attrs.field_name: attrs.field_value},
                sort=[('_id', DESCENDING)]
            )
            print(data)
            try:
                del data['_id']
            except (KeyError, TypeError):
                pass
            return data

    async def update_record(self, attrs: Validatiors.update):
        """"
        using method put
        updates a record which matches the parms passed
        :param attrs:
        :return:
        """
        data = self.db[collection].find_one_and_update({attrs.field_name: attrs.field_value}, {'$set': attrs.data})
        try:
            del data['_id']
        except (KeyError, TypeError):
            pass
        with self.lock:
            return {
                "old value": data
            }


MongoDb = MongoDb()
