import argparse
import logging

import firebase_admin
import pandas as pd
from dotenv import load_dotenv
from firebase_admin import firestore

def upload_to_firebase(dataframe, collection_name, local=False, overwrite=False):
    if local:
        firebase_admin.initialize_app()
    else:
        cred = firebase_admin.credentials.Certificate("./firebase_admin_sdk.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()

    db._firestore_api._target = "localhost:8080"

    logging.info("Uploading data to Firebase...")
    for i, row in dataframe.iterrows():
        data = row.to_dict()
        document_id = data["company_name"].lower().replace(" ", "_").replace("/", "-")
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


if __name__ == "__main__":
    # Argument parser
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--overwrite", action="store_true")
    argparse.add_argument("--local", action="store_true")
    args = argparse.parse_args()
    # Setup
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    # Load CSV data
    def split_string(s):
        return [x.strip() for x in s.split(',')]
    df = pd.read_csv("./companies_db.csv", converters={'tags': split_string})
    # Upload to Firebase
    collection_id = "companies"
    upload_to_firebase(df, collection_id, args.overwrite)
    logging.info("Process completed successfully.")