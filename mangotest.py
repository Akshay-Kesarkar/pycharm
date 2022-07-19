import pymongo



client = pymongo.MongoClient("mongodb+srv://akshay:12345@cluster0.8prah.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d= {
    "name":"akshaykesarkar",
    "email": "akshaykesarkar28@gmail.com",
    "Surname":"kesarkar"
}


d= {
    "name":"akshaykesarkar",
    "email": "akshaykesarkar28@gmail.com",
    "Surname":"kesarkar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )