import requests
from params import user_params

pixela_endpoint = "https://pixe.la/v1/users"
response = requests.post(pixela_endpoint, json=user_params)
print(response.text)