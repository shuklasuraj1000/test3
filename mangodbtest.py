import pymongo

client = pymongo.MongoClient("mongodb+srv://shuklasuraj1000:<password>@cluster0.fjx9k3b.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name' : 'suraj',
    'email' : 'surajshuklashukla582@gmail.com',
    'surname' : 'shukla'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)