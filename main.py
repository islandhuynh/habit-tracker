import requests
from datetime import date
from requests.models import Response
from params import user_params

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(pixela_endpoint, json=user_params)

# graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

# graph_config = {
#   "id": "graph1",
#   "name": "Studying Graph",
#   "unit": "hours",
#   "type": "float",
#   "color": "shibafu"
# }

headers = {
  "X-USER-TOKEN": user_params["token"]
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_config = {
  "date": date.today().strftime("%Y%m%d"),
  "quantity": "5",
}

pixela_add_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/graph1"
response = requests.post(url=pixela_add_endpoint, json=pixel_config, headers=headers)
print(response)