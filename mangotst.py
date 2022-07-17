import pymongo


client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
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
db1 = client['mongotst']
coll = db1['test']
coll.insert_one(d )