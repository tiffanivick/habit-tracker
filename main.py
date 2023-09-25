import requests
from datetime import datetime
import os



USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph2"

pixela_endpoint = os.environ.get("PIXELA_ENDPOINT")


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Job Application Graph",
    "unit": "jobs",
    "type": "int",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
today = datetime.now()
# print(today.strftime("%Y%m%d"))



pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many jobs did you apply for today?")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": '7'
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)