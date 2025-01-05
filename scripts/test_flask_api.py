import requests

# URL of the Flask app
url = 'http://127.0.0.1:5000/predict'
# Data to be sent to the API
data = {'text': 'Great food, excellent service!'}

# Sending post request to the Flask API
response = requests.post(url, json=data)
# Printing the response
print("Status Code:", response.status_code)
print("Response:", response.json())
