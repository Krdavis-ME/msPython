# This code will call the Computer Vision API from Python

# The request library will simplify making a REST API call from Python
# The JSON library is needed to read the data passed back by the web service
import requests
import json

# Access to Computer Vision Service
from dotenv import load_dotenv
load_dotenv()
import os
SUBSCRIPTION_KEY =os.getenv("sub_key")
# Address of Computer Vision Service
vision_service_address = "https://mspythonimageanalyzer.cognitiveservices.azure.com/vision/v2.0/"
# Adding name of the function we are calling to the address
address = vision_service_address + "analyze"

# Three optional parameters: language, details & visualFeatures
parameters = {'visualFeatures': 'Description,Color', 'language': 'en'}

# Open image file to get a file containing an image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# HTTP Headers. Content-Type is application/octet-stream when you pass
#   in a json
headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# HTTP POST
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))