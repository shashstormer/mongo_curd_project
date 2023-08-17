from pymongo import MongoClient
from threading import Lock
from models import Validatiors
from config import db_string, db


class MongoDb:
    def __init__(self):
        self.client = MongoClient(db_string)
        self.db = self.client[db]
        self.lock = Lock()

    async def search(self, attrs: Validatiors.search):
        """
        using method get
        search items with the specified field, value and return one value or all values as specified
        :param attrs:
        :return:
        """
        if attrs.find_all:
            self.db[attrs.collection].find({attrs.field_name: attrs.field_value})
        else:
            self.db[attrs.collection].find_one({attrs.field_name: attrs.field_value})

    async def create_record(self, attrs: Validatiors.create):
        """
        using method post
        adds the data to the specified collection or default collection
        :return:
        """
        with self.lock:
            self.db[attrs.collection].insert_one(attrs.data)

    async def delete_record(self, attrs: Validatiors.delete):
        """
        using method delete
        delets a record which matches the parms passed
        :param attrs:
        :return:
        """
        with self.lock:
            self.db[attrs.collection].find_one_and_delete({attrs.field_name: attrs.field_value})

    async def update_record(self, attrs: Validatiors.update):
        """"
        using method put
        updates a record which matches the parms passed
        :param attrs:
        :return:
        """
        with self.lock:
            self.db[attrs.collection].find_one_and_update({attrs.field_name: attrs.field_value}, {'$set': attrs.data})


MongoDb = MongoDb()
