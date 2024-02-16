import os
from dotenv import load_dotenv
from requests import request

load_dotenv()


def translate(text):
    url = f"{os.getenv('BASE_URL')}/get?q={text}&langpair=en|ru&key={os.getenv('API_KEY')}&de={os.getenv('ADMIN_EMAIL')}"

    res = request(url=url, method="GET")

    return res.json()
