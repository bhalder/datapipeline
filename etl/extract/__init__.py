import pandas as pd
import requests

def extract_from_url(api_url):
    """ Extract data from a given API URL """
    response = requests.get(api_url)
    data = response.json()
    return pd.DataFrame(data)


def extract_from_csv(csv_path):
    """ Extract data from a given CSV file path """
    return pd.read_csv(csv_path)