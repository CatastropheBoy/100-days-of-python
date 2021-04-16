from datetime import datetime
import requests

USERNAME = "catastropheboy"
TOKEN = "345wertdfgbvcx"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# resp = requests.post(url=pixela_endpoint, json=user_params)
# print(resp.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_header = {
#     "X-USER-TOKEN": TOKEN
    # }


graph_params = {
    "id": "tinker1",
    "name": "Tinkering Graph",
    "unit": "Day",
    "type": "int",
    "color": "ajisai"
}


# graph_resp = requests.post(url=graph_endpoint, json=graph_params, headers=graph_header)
# print(graph_resp.status_code)
now = datetime.now()
today = now.strftime("%Y%m%d")

def post_pixel(date, quantity, graph):
    pixel_header = {
        "X-USER-TOKEN": TOKEN
    }

    pixel_params = {
        "date": date,
        "quantity": str(quantity)
    }

    endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph}"
    return requests.post(
        url=endpoint, json=pixel_params, headers=pixel_header
        )

# post_pixel(today, 1, "tinker1")

def update_pixel(date, quantity, graph):
    pixel_header = {
        "X-USER-TOKEN": TOKEN
    }

    pixel_params = {
        "quantity": str(quantity)
    }

    endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph}/{date}"
    return requests.put(
        url=endpoint, json=pixel_params, headers=pixel_header
        )

# update_pixel(today, 300, "tinker1")

def delete_pixel(date, graph):
    pixel_header = {
        "X-USER-TOKEN": TOKEN
    }

    endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph}/{date}"
    return requests.delete(
        url=endpoint, headers=pixel_header
        )

delete_pixel(today, "tinker1")