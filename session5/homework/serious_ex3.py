from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]
customers = db['customers']

manh_post = {
    'title': 'Job requirement',
    'author': 'c4e21_manhducpham',
    'content': '''
    In-charge of finance sector of a specific group of subsidiaries or a subsidiary at Vingroup, including but not limited to:
    o   Finance strategy
    o   Finance management
    o   Accounting management
    o   Risk management
    -          In-charge of all aspects of finance department, including but not limited to:
    o   Planning
    o   Human resource
    o   Regulation & policies
    o   Finance
    o   Legal
    o   Auditing
    o   Risk management''',
}
posts.insert_one(manh_post)