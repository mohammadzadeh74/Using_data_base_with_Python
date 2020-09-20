import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydb"]

print(myclient.list_database_names())

my_dbs = myclient.list_database_names()

print(mydb.list_collection_names())

mycol = mydb["testCollection"]

for x in mycol.find({},{ "_id": 0}):
  	print(x)


print(mycol.find({},{ "_id": 0})[1])


for x in mycol.find({},{ "_id": 0 }):
	 print(x)


myquery = { "month" : 7}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
