import json
from json import JSONDecodeError
import requests



def get_config(path: str = "config.json") -> dict:
    try:

        with open(path, "r") as f:
            data = json.loads(f.read())

        return data

    except FileNotFoundError as e:
        print(f"Please add the config file. {e}")
        return {}
    except JSONDecodeError as e:
        print(f"Please check the json from config file because it is not valid. {e}")
        return {}



def get_quote(url: str) -> dict:
    response = requests.get(url)
    if str(response.status_code).startswith("2"):
        if response.text:
            response_data = json.loads(response.text)
            quote = response_data['sentence']
            name = response_data['character']['name']
            house = response_data['character']['house']['name']

            return {"quote": quote, "name": name, "house": house}

if __name__ == '__main__':
    config = get_config()
    if config:
        while True:
            data = get_quote(config['url'])
            text = f"""
            Quote: {data['quote']}
            Who said it? {data['name']}
            House: {data['house']} 
            """
            print(text)
            user_input = input("Do you want another quote? Y/N")
            if user_input.lower() == "n":
                break