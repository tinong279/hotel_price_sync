import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

api_base = os.getenv("WP_API_BASE")
username = os.getenv("WP_USERNAME")
app_password = os.getenv("WP_APP_PASSWORD")
timeout = int(os.getenv("REQUEST_TIMEOUT", "30"))
user_agent = os.getenv("USER_AGENT", "Mozilla/5.0")

url = f"{api_base}/users/me"

response = requests.get(
    url,
    auth=HTTPBasicAuth(username, app_password),
    timeout=timeout,
    headers={"User-Agent": user_agent},
)

print("Status Code:", response.status_code)
print(response.text)