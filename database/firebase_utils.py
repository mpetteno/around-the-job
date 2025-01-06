import logging

import firebase_admin
from firebase_admin import firestore


def get_firebase_client():
    cred = firebase_admin.credentials.Certificate("./firebase_admin_sdk.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def write_document(db, data, collection_name, document_id, overwrite=False):
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()
    if doc.exists and not overwrite:
        logging.info(f"Document {document_id} already exists. Skipping.")
    else:
        db.collection(collection_name).document(document_id).set(data)
        if overwrite:
            logging.info(f"Overwritten document {document_id}.")
        else:
            logging.info(f"Uploaded document {document_id}.")
