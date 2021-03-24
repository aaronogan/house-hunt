import requests

class RapidApi:
    def __init__(self, config):
        self.config = config

    def get_endpoint_url(self, endpoint_name=''):
        return ''.join((self.config['base-url'], endpoint_name))

    def get_headers(self):
        return self.config['headers']

    def http_get(self, endpoint_name='', params={}):
        endpoint_url = self.get_endpoint_url()
        headers = self.get_headers()

        response = requests.request("GET", endpoint_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("There was a problem retrieving data", endpoint_url, headers, params)

