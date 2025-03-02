import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Income"]
collection = db["Data"]

# Load CSV file
df = pd.read_csv(r"C:\Users\ACER PREDATOR\Desktop\Machine_learning Bootcamp\Database(MongoDB)\adult.data")

data = df.to_dict(orient="records")  # Convert to list of dictionaries

# Insert into MongoDB
collection.insert_many(data)

print("CSV dataset inserted successfully!")
