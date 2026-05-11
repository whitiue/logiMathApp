import requests

API_BASE_URL = "http://localhost:8000"


def get_quizzes():
    return requests.get(f"{API_BASE_URL}/quizzes")


def create_user(name, email):
    return requests.post(
        f"{API_BASE_URL}/users",
        params={
            "name": name,
            "email": email,
        },
    )