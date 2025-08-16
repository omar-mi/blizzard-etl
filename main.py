import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "http://api.marketstack.com/v1/"
endpoint = "eod"
full_url = base_url + endpoint

params = {
    "access_key": api_key,
    "symbols": "AAPL"   
}

response = requests.get(full_url, params=params)
