from pymongo import MongoClient

def get_test_data_from_mongo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['api_test_db']
    collection = db['test_data']

    # Assuming test data is stored in a collection in MongoDB
    data = collection.find()
    test_data = [(entry['test_case_id'], entry['endpoint']) for entry in data]
    return test_data
