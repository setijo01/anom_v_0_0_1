import pymongo
import os


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['setiawan']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        return Database.DATABASE[collection].update_one(query, data, upsert=False)

    @staticmethod
    def delete(collection, query):
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def sort(collection, sort_query, num):
        return Database.DATABASE[collection].find().sort(sort_query, num)