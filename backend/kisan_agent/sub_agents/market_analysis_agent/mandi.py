# import requests
# i=0
# print(f'ok {i}')
# i+=1
# # API endpoint and parameters
# url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
# params = {
#     "api-key": "579b464db66ec23bdd000001de5b9efe20fe44f273570082d48519b7",
#     "format": "json",  # use 'json' for easy parsing
#     "limit": 1       # number of records to fetch, change as needed
# }
# print(f'ok {i}')
# i+=1

# # Send GET request
# response = requests.get(url, params=params)
# print(f'ok {i}')
# i+=1

# # Check response status
# if response.status_code == 200:
#     print(f'ok {i}')
#     i+=1

#     data = response.json()
#     print(f'ok {i}')
#     i+=1

#     # Print full data (or handle as per need)
#     print("Total records fetched:", len(data.get("records", [])))
#     print(f'ok {i}')
#     i+=1

#     for record in data["records"]:
#         print(
#             f"State: {record['state']}, District: {record['district']}, Market: {record['market']}, "
#             f"Commodity: {record['commodity']}, Variety: {record['variety']}, Grade: {record['grade']}, "
#             f"Arrival Date: {record['arrival_date']}, Min Price: {record['min_price']}, "
#             f"Max Price: {record['max_price']}, Modal Price: {record['modal_price']}"
#         )
# else:
#     print("Error:", response.status_code,response.text)
    
    
import requests
try:
    response = requests.get("https://www.google.com", timeout=5) # Add a timeout for quicker feedback
    if response.status_code == 200:
        print("Successfully connected to Google!")
    else:
        print(f"Failed to connect to Google: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Could not connect to Google: {e}")