import pymongo
mongodb = pymongo.MongoClient("mongodb://localhost:27017/")
db_tushare = mongodb["tushare"]
collection_tushare = db_tushare["tushare"]