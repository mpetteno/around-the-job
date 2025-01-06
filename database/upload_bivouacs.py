import argparse
import logging

import pandas as pd
from dotenv import load_dotenv

from database.firebase_utils import write_document, get_firebase_client


def upload_bivouacs(db, dataframe, collection_name, overwrite=False):
    logging.info("Uploading bivouacs to Firebase...")
    for _, row in dataframe.iterrows():
        data = row.to_dict()
        document_id = data["name"].lower().replace(" ", "_").replace("/", "-")
        write_document(db, data, collection_name, document_id, overwrite)

if __name__ == "__main__":
    # Argument parser
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--overwrite", action="store_true")
    args = argparse.parse_args()
    # Setup
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    # Get firebase client
    fb_client = get_firebase_client()
    # Upload companies
    df = pd.read_csv("./bivouacs_db.csv")
    collection_id = "bivouacs"
    upload_bivouacs(fb_client, df, collection_id, args.overwrite)
