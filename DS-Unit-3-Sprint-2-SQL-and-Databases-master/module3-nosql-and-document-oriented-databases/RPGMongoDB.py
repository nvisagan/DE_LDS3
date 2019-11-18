# username:
# password: 

import pymongo

#Full Driver from MongoDB
client = pymongo.MongoClient("mongodb+srv://<username>:<pass>@lambda-axnyh.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

#Count of documents
db.test.count_documents({'x': 1})

#Inserting a document
db.test.insert_one({'x': 1})

#Count of documents
db.test.count_documents({'x':1})

#Inserting a document - NOTE different memory address
db.test.insert_one({'x': 1})

#Count of documents increased, but each one is unique at a different memory address
db.test.count_documents({'x': 1})

#Finding one of the objects
db.test.find_one({'x': 1})

#Finding this is assignted to a cusor!
curs = db.test.find({'x': 1})

#The list of all the objects within the cursor
list(curs)

#create some test objects
navo_doc = {
    'favorite_animal': 'Doge'
}

bobs_doc = { 
    'favorite_animal': 'Cat',
    'favorite_color': ' Blue'
}

alice_doc = {
    'favorite_animal': 'Ape'
}

#importing new docs above into the database
#Note DONE TWICE
db.test.insert_many([navo_doc, bobs_doc, alice_doc])

#list all the objects in the database
list(db.test.find())

#creating more test documents
more_docs = []
for i in range(10):
  doc = {'even': i% 2 == 0}
  doc['value'] = i
  more_docs.append(doc)

more_docs

#inserting test documents into the database
db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

# the update one function takes a filter and updates a single document that matches that filter.
# incrementing the field that is value 3 and incrementing it by 5
db.test.update_one({'value':3},
                   {'$inc': {'value':5}})

#look, value 3 is now value 5!                   
list(db.test.find({'value':3}))

#Incrementing all of the even fields = true by 100
db.test.update_many({'even':True},
                   {'$inc': {'value':100}})                   
list(db.test.find({'even':True}))

#lets try deleting all files that are even = false
db.test.delete_many({'even':False})

#lets add an rpg character from yesterday's assignment!
rpg_char = (1, "King Bob", 10,3,0,0,0)

#we can insert it as a very simple one key python dict as shown here...
db.test.insert_one({"rpg_char" : rpg_char})

#this might not be the best way to organize it though...
#this will break out each variable as a key within a dictionary.
db.test.insert_one({
    'sql_id': rpg_char[0],
    'name': rpg_char[1],
    'hp' : rpg_char[1]
})

list(db.test.find())