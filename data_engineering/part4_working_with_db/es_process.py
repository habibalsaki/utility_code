from elasticsearch import Elasticsearch, helpers
from faker import Faker

fake = Faker()
es = Elasticsearch()


actions = [
    {
        "_index": "users",
        "_type": "doc",
        "_source": {
            "name": fake.name(),
            "street": fake.street_address(),
            "city": fake.city(),
            "zip": fake.zipcode()
        }
    }
    for j in range(1000)
]

# res = helpers.bulk(es, actions)
# print(res['result'])

doc = {
    "query": {
        "match_all": {}
    }
}

res = es.search(index="users",body=doc,size=10)

for doc in res['hits']['hits']:
    print(doc['_source'])