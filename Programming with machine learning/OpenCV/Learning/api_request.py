import requests
import json

# API endpoint
url = "https://api-d7b62b.stack.tryrelevance.com/latest/studios/c5245b63-b594-45bf-a5b7-63d14cf9141e/trigger_limited"

# Request headers
headers = {
    "Content-Type": "application/json",
}

# Request body
payload = {
    "params": {
        "file_url": "your_file_url",
        "data_points": ["data_point_1", "data_point_2"],
        "llm_choice": "your_llm_choice"
    },
    "project": "fad029bba47b-4bcc-9ae0-d10a810b2a03"
}

# Convert payload to JSON
payload_json = json.dumps(payload)

# Make the API request
response = requests.post(url, headers=headers, data=payload_json)

# Print the response
print("Response Code:", response.status_code)
print("Response Body:", response.text)
