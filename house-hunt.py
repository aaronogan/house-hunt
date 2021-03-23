import requests
import yaml
from abc import ABC, abstractmethod

class RapidApi:
    def __init__(self, config):
        self.config = config

    def get(self, endpoint_url, headers, params):
        response = requests.request("GET", endpoint_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("There was a problem retrieving data", endpoint_url, headers, params)


class RealEstateApi:
    def __init__(self):
        pass

    @abstractmethod
    def get_listings(self):
        raise NotImplementedError


class RealtorFreeRealEstateApi(RapidApi, RealEstateApi):
    def __init__(self, config):
        RapidApi.__init__(self, config)
        RealEstateApi.__init__(self)

    def get_listings(self):
        base_url = self.config['base-url']
        endpoint_url = ''.join((base_url, "properties"))

        headers = self.config['headers']

        querystring = {
            "city": "Denver",
            "state_code": "CO",
            "offset": "0",
            "limit": "15"
        }

        json_response = self.get(endpoint_url, headers, querystring)
        return json_response


def get_config():
    file_name = "config.yml"
    with open(file_name, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as ex:
                print(ex)
                return None

if __name__ == "__main__":
    config = get_config()

    realtor_free_config = config['apis']['rapidapi']['realtor-free']
    realtor_api = RealtorFreeRealEstateApi(realtor_free_config)

    print(realtor_api.get_listings())


