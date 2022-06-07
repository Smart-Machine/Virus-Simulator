import requests
import json


URL = 'http://127.0.0.1:5000/data'


def parse(text: str) -> dict:

    text = text.split("[")[1].split("]")[0].split(",")

    data = []
    i = 0
    while (i < len(text)-1):
        data.append(json.loads(f"{text[i]},{text[i+1]}"))
        i += 2

    return data 


def get(url: str = URL) -> None:

    response = requests.get(url)
    data = parse(response.text)
    print(data)


if __name__=='__main__':
    get()
