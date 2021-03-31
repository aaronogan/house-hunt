from model.rapidapi import RapidApi
from model.realestateapi import RealEstateApi
from model.realestatelisting import RealEstateListing

class RealtorRealEstateApi(RapidApi, RealEstateApi):
    def __init__(self, config):
        RapidApi.__init__(self, config)
        RealEstateApi.__init__(self)

    def http_get_listings(self, search):
        endpoint_url = self.get_endpoint_url("for-sale")
        headers = self.config['headers']

        querystring = search.to_json()
        json_response = self.http_get(endpoint_url, querystring)

        if json_response['status'] == 200:
            data = json_response['data']
            return [RealEstateListing(listing) for listing in data['results']]
        else:
            return []
