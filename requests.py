import requests

# URL to make a GET request to
url = "https://github.com/VixoTheDev/Python"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Response JSON:")
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
