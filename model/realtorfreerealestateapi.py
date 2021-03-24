import model.RapidApi
import model.RealEstateApi

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

