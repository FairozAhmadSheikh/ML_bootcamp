import pymongo

try:
    client=pymongo.MongoClient("mongodb://localhost:27017")
    client.server_info()    
    print("database conneted ")

except Exception as e:
    print("connection establishment failed ",e)


#  get database names 
def get_database_names():
    dbs=client.list_database_names()
    print("The Databases are : ")
    for name in dbs:
        print(name)

# get_database_names()

# finding things from collection

database=client["NexonDB"]
collection=database["Prods"]

 # greater than 

# res=collection.find({"age":{"$gt":21}}) 

# for i in res:
#     print(i)

 # acessending order

# ress=collection.find().sort("age") 
# for i in ress:
#     print(i)

 # descending order

# ress=collection.find().sort("age",-1) 
# for i in ress:
#     print(i)