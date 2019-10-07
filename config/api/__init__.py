import requests
from requests.exceptions import HTTPError

class WordApi:
    api_base_url = 'http://random-word-api.herokuapp.com'
    api_token = 'jecgaa'

    @staticmethod
    def get_word():
        url = '/word'
        try:
            response = requests.get(WordApi.api_base_url+url, params={'key': WordApi.api_token})
            response.raise_for_status()
            if response:
                json_response = response.json()
                print("getting word", json_response[0])
                return json_response[0]
            else:
                return None
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
