import os
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

api_base = os.getenv("WP_API_BASE")
post_type = os.getenv("WP_POST_TYPE")
username = os.getenv("WP_USERNAME")
app_password = os.getenv("WP_APP_PASSWORD")
hotel_post_id = os.getenv("HOTEL_POST_ID")
timeout = int(os.getenv("REQUEST_TIMEOUT", "30"))
user_agent = os.getenv("USER_AGENT", "Mozilla/5.0")

if not all([api_base, post_type, username, app_password, hotel_post_id]):
    raise ValueError("請先檢查 .env，缺少必要設定")

url = f"{api_base}/{post_type}/{hotel_post_id}"

# 先讀目前資料，避免覆蓋掉其他 ACF 欄位
get_response = requests.get(
    url,
    timeout=timeout,
    headers={"User-Agent": user_agent},
)
get_response.raise_for_status()

current_data = get_response.json()
current_acf = current_data.get("acf", {})

print("Before update:")
print("Agoda Price:", current_acf.get("agoda_price"))
print("Booking Price:", current_acf.get("booking_price"))
print("Last Updated:", current_acf.get("last_updated"))
print("Source URL:", current_acf.get("source_url"))

updated_acf = current_acf.copy()
updated_acf["agoda_price"] = 3999
updated_acf["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

payload = {
    "acf": updated_acf
}

update_response = requests.post(
    url,
    auth=HTTPBasicAuth(username, app_password),
    json=payload,
    timeout=timeout,
    headers={
        "User-Agent": user_agent,
        "Content-Type": "application/json",
    },
)

print("\nUpdate status code:", update_response.status_code)
print("Raw response:", update_response.text)

update_response.raise_for_status()

updated_data = update_response.json()
updated_result = updated_data.get("acf", {})

print("\nAfter update:")
print("Agoda Price:", updated_result.get("agoda_price"))
print("Booking Price:", updated_result.get("booking_price"))
print("Last Updated:", updated_result.get("last_updated"))
print("Source URL:", updated_result.get("source_url"))