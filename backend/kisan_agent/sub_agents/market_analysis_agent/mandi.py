
import requests

# ---------------- CONFIG ----------------
url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
api_key = "579b464db66ec23bdd000001de5b9efe20fe44f273570082d48519b7"
TARGET_STATE = "Uttar Pradesh"
limit = 100
# ----------------------------------------

def fetch_mandi_data(state: str = TARGET_STATE):
    offset = 0
    all_records = []

    while True:
        params = {
            "api-key": api_key,
            "format": "json",
            "limit": limit,
            "offset": offset,
            "filters[state]": state
        }

        response = requests.get(url, params=params)

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
