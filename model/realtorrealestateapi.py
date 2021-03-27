from model.rapidapi import RapidApi
from model.realestateapi import RealEstateApi
from model.realestatelisting import RealEstateListing

class RealtorRealEstateApi(RapidApi, RealEstateApi):
    def __init__(self, config):
        RapidApi.__init__(self, config)
        RealEstateApi.__init__(self)

    def http_get_listings(self, search):
        base_url = self.config['base-url']
        endpoint_url = ''.join((base_url, "properties"))

        headers = self.config['headers']

        querystring = {
            "city": "Denver",
            "state_code": "CO",
            "offset": "0",
            "limit": "15"
        }

        json_response = self.http_get(endpoint_url, querystring)

        if json_response['status'] == 200:
            data = json_response['data']
            return [RealEstateListing(listing) for listing in data['results']]
        else:
            return []
