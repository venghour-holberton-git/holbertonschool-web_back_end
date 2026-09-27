from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:27027/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.12.0")
db = client.apple_dataa
collection = db.test_collection
fav = {
    "name": "mana",
    "favorite": "bird"
}
collection.insert_one(fav)
collections = collection.find()
for i in collections:
    print(i)