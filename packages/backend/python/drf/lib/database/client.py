from pymongo import MongoClient
def get_db():
    client = MongoClient(host='localhost',
                        port=int('27020'),
                        username='root',
                        password='password'
                        )
    db_handle = client['caro']
    collections = ["users", "changeevents", "positions", "requisitions"]
    for collection in collections:
        if collection not in db_handle.list_collection_names():
            db_handle.create_collection(collection)
    return db_handle

