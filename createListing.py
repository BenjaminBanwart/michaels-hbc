from dotenv import load_dotenv
import os
import requests

load_dotenv()

prefix = "https://www.michaels.com/api/mkp/v1/"
API_KEY = os.getenv("API_KEY")

response = requests.get(prefix + "listing/all-listings",
    headers={"Api-Key": API_KEY})

print(response.json())