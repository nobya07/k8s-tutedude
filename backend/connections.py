from pymongo import MongoClient
from os import environ

MONGO_HOST = environ.get('MONGO_HOST', 'localhost')

clinent = MongoClient(MONGO_HOST, 27017)

db = clinent['ires']

coll=db['names']