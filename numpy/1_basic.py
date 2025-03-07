import pandas as pd 


listt=[7,8,9,6,4,5,6,2,1,3,0,11]

# How To create a DataFrame using a list
dataframe=pd.DataFrame(listt)
print(dataframe)


data2=[["sunnt",26],["manish",23],["aariya",21]]

dataframe1=pd.DataFrame(data2,columns=["name","age"])
print(dataframe1)


# How To create a DataFrame using a dictionary

data3={
    "Names":["Satish","Nishant","Asish"],
    "Age":[27,28,21],
    "Gender":["M","F","F"]
}

data_frame3=pd.DataFrame(data3,columns=["Names","Age"],index=["student1","student2","student3"])

print(data_frame3)

# Creating A Dataframe using list with multiple dictionary

data4=[{"col1":22,"col2":23},{"col1":23,"col2":25,"col3":27}]

dataframe_4=pd.DataFrame(data4)
print(dataframe_4)
