import requests

def retrieve_data():
    # Define the API endpoint and payload (data)
    url = "https://threatfox-api.abuse.ch/api/v1/"
    payload = {
        "query": "get_iocs",
        "payload": "win",
        "days": 1
    }

    # Send the POST request to the API
    response = requests.post(url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and return the response data (JSON format)
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
