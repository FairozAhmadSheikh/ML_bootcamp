import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

#database 
dataBase=client["NexoDB"]

# collection
collection=dataBase["Products"]

#sample data
data={
    "Name":"Ali",
    "Roll_no":121,
    "Batch":2016,
    "email":"Ali@gmail.com",
    "password":"786@123"
}

# Insert data into database

collection.insert_one(data)