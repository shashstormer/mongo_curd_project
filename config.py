import os


class DatabaseNotSet(Exception):
    def __init__(self):
        print("Set Database String in environment to variable database_string")
        self.message = "Database String Not set in env variable"
        super().__init__(self.message)


db_string = os.getenv("database_string")
if db_string is None:
    raise DatabaseNotSet
db = os.getenv("database_name", "records_db")
force_collection_name = os.getenv("collection_name")
