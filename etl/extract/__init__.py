import pandas as pd
import requests

def extract_data(api_url):
    """ Extract data from a given API URL """
    response = requests.get(api_url)
    data = response.json()
    return pd.DataFrame(data)
