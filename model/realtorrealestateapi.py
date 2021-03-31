from model.rapidapi import RapidApi
from model.realestateapi import RealEstateApi
from model.realestatelisting import RealEstateListing

class RealtorRealEstateApi(RapidApi, RealEstateApi):
    def __init__(self, config):
        RapidApi.__init__(self, config)
        RealEstateApi.__init__(self)

    def http_get_listings(self, search):
        return self.http_get("for-sale", search.to_json())

