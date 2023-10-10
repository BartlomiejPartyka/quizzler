import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

data = requests.get(url='https://opentdb.com/api.php', params=parameters)
data.raise_for_status()
questions = data.json()
question_data = questions['results']
