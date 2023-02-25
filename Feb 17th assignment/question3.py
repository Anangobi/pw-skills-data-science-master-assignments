client = pymongo.MongoClient("mongodb+srv://gobianan:gobianan@cluster0.dzwhgbn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db=client["gobi_test1"]
col_gobi=db["gobi"]
