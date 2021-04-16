import requests
import html

params = {
    'amount': 10,
    'type': 'boolean'
}
resp = requests.get(url='https://opentdb.com/api.php', params=params)
resp.raise_for_status()


question_data = resp.json()['results']
