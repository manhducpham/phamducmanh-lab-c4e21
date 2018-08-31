from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]
customers = db['customers']

customer_list = customers.find()
# for i in customer_list:
#     print(i)

ref_count = [0, 0, 0]
for customer in  customer_list:
    if customer['ref'] == 'events':
        ref_count[0] += 1
    elif customer['ref'] == 'ads':
        ref_count[1] += 1
    else:
        ref_count[2] += 1
print(ref_count)
ref_labels = ['events', 'ads', 'wom']
pyplot.pie(ref_count, labels = ref_labels, autopct = "%.1f%%", shadow = True, explode = [0, 0, 0.2])
pyplot.title('wom vs. events, ads references')
pyplot.axis('equal')
pyplot.show()