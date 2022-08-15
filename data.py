import requests


def get_quiz_questions():
    api_endpoint = "https://opentdb.com/api.php"
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url=api_endpoint, params=parameters)
    response.raise_for_status()
    return response.json()["results"]


question_data = get_quiz_questions()
