from bson import ObjectId
from model import collection

def get_entries():
    entries = list(collection.find())
    entries_json = [{'_id': str(entry['_id']), 'time': str(entry['time']), 'date': str(entry['date'])} for entry in entries]
    return entries_json

def add_entry(date, time):
    collection.insert_one({'time': time, 'date': date})

def edit_entry(id, date, time):
    collection.update_one({'_id': ObjectId(id)}, {'$set': {'time': time, 'date': date}})

def delete_entry(id):
    collection.delete_one({'_id': ObjectId(id)})
