import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["instrumentosdb"]
col = db["instrumentos"]


def collectionInstrumentos():
    try:
        return col
    except Exception as ex:
        print(ex)


def dbFromMongoDB():
    try:
        return db
    except Exception as ex:
        print(ex)


def clientFromMongoDB():
    try:
        return client
    except Exception as ex:
        print(ex)
