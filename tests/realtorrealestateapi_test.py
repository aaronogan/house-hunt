from model.realtorrealestateapi import RealtorRealEstateApi
from model.realestatelisting import RealEstateListing
from model.realestatesearch import RealEstateSearch

sample_api_config = {
    "base-url": "some-url",
    "headers": {
    }
}

sample_listings = [{
    "list_date": "2020-10-24T023:01:38Z",
    "list_price": 230000,
    "listing_id": "1212",
    "property_id": "1234",
    "status": "for_sale",
}]

sample_response = {
    "data": {
        "count": 1,
        "results": sample_listings,
    },
    "status": 200,
}

class RealtorRealEstateApiWrapper(RealtorRealEstateApi):
    def __init__(self, config):
        RealtorRealEstateApi.__init__(self, config)

    def http_get(self, endpoint_name='', params={}):
        return sample_response

def test_returns_listing_type():
    real_estate_api = RealtorRealEstateApiWrapper(sample_api_config)
    real_estate_search = RealEstateSearch()
    listings = real_estate_api.http_get_listings(real_estate_search)

    assert isinstance(listings[0], RealEstateListing)

