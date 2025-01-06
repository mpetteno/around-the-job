import argparse
import logging

import numpy as np
import pandas as pd
from dotenv import load_dotenv

from database.firebase_utils import write_document, get_firebase_client


def upload_companies(db, dataframe, collection_name, overwrite=False):
    logging.info("Uploading companies to Firebase...")
    for _, row in dataframe.iterrows():
        data = row.to_dict()
        document_id = data["company_name"].lower().replace(" ", "_").replace("/", "-")
        write_document(db, data, collection_name, document_id, overwrite)


def upload_tags(db, dataframe, collection_name, overwrite=False):
    logging.info("Uploading tags to Firebase...")
    unique_tags = np.unique(np.concatenate(dataframe['tags']))
    for tag in unique_tags:
        data = { "name": tag }
        document_id = tag.lower().replace(" ", "_").replace("/", "-")
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
    # Upload tags
    def split_string(s):
        return [x.strip() for x in s.split(',')]
    df = pd.read_csv("./companies_db.csv", converters={'tags': split_string})
    collection_id = "companies_tags"
    upload_tags(fb_client, df, collection_id, args.overwrite)
    logging.info("Process completed successfully.")
    # Upload companies
    def tags_to_map(s):
        return {x.strip(): True for x in s.split(',')}
    df = pd.read_csv("./companies_db.csv", converters={'tags': tags_to_map})
    collection_id = "companies"
    upload_companies(fb_client, df, collection_id, args.overwrite)
