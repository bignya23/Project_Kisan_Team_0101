import requests
from dotenv import load_dotenv
import os

load_dotenv()

url=os.getenv("URL")

api_key=os.getenv("API")

# ---------------- CONFIG ----------------

TARGET_STATE = "Uttar Pradesh"
limit = 100
# ----------------------------------------

def fetch_mandi_data(state: str = TARGET_STATE):
    print("ok1")
    offset = 0
    all_records = []

    while True:
        print("ok2")
        params = {
            "api-key": api_key,
            "format": "json",
            "limit": limit,
            "offset": offset,
            "filters[state]": state
        }
        print("ok3")
        # response = requests.get(url, params=params)

        print("ok4")

        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])

            if not records:
                break

            all_records.extend(records)

            if len(records) < limit:
                break

            offset += limit
        else:
            print(f"Error fetching data for {state}: {response.status_code}")
            break

    return all_records

if __name__ == '__main__':
    records = fetch_mandi_data()
    if records:
        print(f"\n✅ Prices in {TARGET_STATE} ({len(records)} records):")
        for r in records:
            print(f"{r['commodity']} ({r['variety']}): ₹{r['min_price']} - ₹{r['max_price']} (Modal: ₹{r['modal_price']}) | Market: {r['market']}, District: {r['district']}")
