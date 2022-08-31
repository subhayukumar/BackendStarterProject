import firebase_admin
from firebase_admin import credentials, firestore
import os

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)
db = firestore.client()  # this connects to our Firestore database

def get_state(x: str):
    collection = db.collection('collection1')
    doc = collection.document(x)
    res = doc.get().to_dict()
    return res
