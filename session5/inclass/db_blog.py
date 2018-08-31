### step by step
# step 1: connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId
#pymongo => db driver
uri = "mongodb://king_k0m4:Manpro12babon@ds029224.mlab.com:29224/c4e_21"

client = MongoClient(uri)
db = client.get_default_database()
# step 2: select collection
posts = db["posts"] # co roi thi tao ra, neu khong thi tao moi
print(posts)
# step 3: create document
post = {
    'title': 'Cuoc doi lam doi bat cong',
    'content': 'Thang hai hop sua thang khong hop nao',
}

# step 4: insert document
# posts.insert_one(post)

# print('done!')

# find all
# post_list = posts.find()
# for post in post_list: #post_list ~ collection ~ list
#     print(post) # post ~ document ~ dictionary
# find one: tra ve cai dau tien python tim thay, neu khong co gi thi la bai post dau tien
# cond = {
#     '_id': ObjectId("5b855876d7bca007acfc0f26"), # phai import object id
# }
# post = posts.find_one(cond)
# print(post)

# tim gan dung
cond = {
    'title': {
        '$regex': "hom",    # abbriviation: Regular Expression
        '$options': "i",    # ignore case: cap vs lower
    }
}
post = posts.find_one(cond)
print(post)
