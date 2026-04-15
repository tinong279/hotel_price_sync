import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

api_base = os.getenv("WP_API_BASE")
post_type = os.getenv("WP_POST_TYPE")
username = os.getenv("WP_USERNAME")
app_password = os.getenv("WP_APP_PASSWORD")
hotel_post_id = os.getenv("HOTEL_POST_ID")
timeout = int(os.getenv("REQUEST_TIMEOUT", "15"))

url = f"{api_base}/{post_type}/{hotel_post_id}"

response = requests.get(
    url,
    auth=HTTPBasicAuth(username, app_password),
    timeout=timeout,
    headers={"User-Agent": os.getenv("USER_AGENT", "Mozilla/5.0")}
)

print("Status Code:", response.status_code)
response.raise_for_status()

data = response.json()
acf = data.get("acf", {})

print("Hotel ID:", data.get("id"))
print("Title:", data.get("title", {}).get("rendered"))
print("Agoda Price:", acf.get("agoda_price"))
print("Booking Price:", acf.get("booking_price"))
print("Last Updated:", acf.get("last_updated"))
print("Source URL:", acf.get("source_url"))