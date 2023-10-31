"""
Software 2 - Python Module 12
Using external interfaces
"""

# Task 1
import json

import requests

request = "https://api.chucknorris.io/jokes/random"

response = requests.get(request).json()

print(response['value'])

print(json.dumps(response, indent=2))

