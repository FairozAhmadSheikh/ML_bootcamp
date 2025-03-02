import pymongo
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    client.server_info()
    print("Connection Successfull ")
except Exception as e:
    print("Connection Establishment Failed ! ",e)

# create Database
database=client["NexonDB"]

# create collection
collection=database["Prods"]

# Function to insert data based on consent 
def insert():
    name=input("Enter Username : ")
    password=input("Create a Password : ")
    email=input("enter Email : ")
    age=int(input("Enter age in Years : "))
    d1={
        "name":name,
        "password":password,
        "email":email,
        "age":age
    }
    collection.insert_one(d1)
    return "Success"

# Function to fetch data whole
def get_det():
    data=collection.find()
    for val in data :
        print(val)
# Function to fetch single entry
def single_ent():
    name=input("enter name to find : ")
    found=collection.find_one({"name":name})
    if found:
        for i,j in found.items():
            print(i," : ",j)
    else:
        print("No record with that name ")

# function to delete 
def delete():
    name=input("Enter Name you want to delete Entry of : ")
    if collection.find_one({"name":name}):
        deleted=collection.delete_one({"name":name})
        print("deleted sucessfully ",deleted)
    else:
        print("Name Not Found")
    get_det()

# function to update
def update():
    name=input("Enter name you want to update age for : ")
    new_age=int(input("enter updated  age (new age) :  "))
    if collection.find_one({'name':name}):
        collection.update_one({"name": name}, {"$set": {"age": new_age}})
        print("age Updated Successfully")
    else:
        print("Name not found")

consent=input("""
if you want to store data to DB             : Enter Y 
if you want to view Data Base fully         : Enter V 
if you want to find some single entry       : Enter S
if you want to return without any operation : Enter Q 
if you want to DELETE  entry based on name  : Enter D 
if you want to UPDATE  entry based on name  : Enter U 
              """).lower()
if consent=="y":
    print(insert())
elif consent=="v":
    get_det()
elif consent=="s":
    single_ent()
elif consent=="d":
    delete()
elif consent=="u":
    update()
else:
    print("Thank You Visit again")