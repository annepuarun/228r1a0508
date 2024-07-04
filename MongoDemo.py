import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_name())
mydb=myclient["cmrec"]

mycol=mydb["csea"]
'''
mylist=mydb.list_collection_names()
if"csea"in mylist:
    print("is exist")
else:
    print("Does'nt exist")'''
mydict={"name":"shekar","Rollno":"228r1a0554"}
x=mycol.insert_one(mydict)
x=