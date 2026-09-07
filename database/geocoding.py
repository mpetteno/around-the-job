import logging
import os

import pandas as pd

from dotenv import load_dotenv
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut

def geocode_address(address, geolocator, retry_count=3):
    for attempt in range(retry_count):
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                return location.latitude, location.longitude
        except GeocoderTimedOut:
            logging.warning(f"Geocoding timed out for address {address} (try {attempt}).")
            continue
    logging.warning(f"Geocoding is null for address {address}.")
    return None, None

def add_coordinates(dataframe):
    logging.info("Geocoding addresses...")
    api_key = os.getenv('GOOGLE_API_KEY') or ""
    geolocator = GoogleV3(api_key=api_key)
    for i, address in enumerate(dataframe["headquarter_address"]):
        lat, lng = geocode_address(address, geolocator)
        dataframe.loc[i, "latitude"] = lat
        dataframe.loc[i, "longitude"] = lng
        logging.info(f"Processed: {address} -> Lat: {lat}, Lng: {lng}")
    return dataframe


if __name__ == "__main__":
    # Setup
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    file_id = "1eLd29yh5NUb7R3_4S_UUC7T9rS8D-ItcK-09ROjl6bw"
    file_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx"
    logging.info(f"File URL: {file_url}")
    # Load CSV data
    df = pd.read_excel(file_url)
    # Add Coordinates
    df_with_coords = add_coordinates(df)
    df_with_coords.to_excel("companies_db_modified.xlsx", index=False)
    logging.info("Process completed successfully.")