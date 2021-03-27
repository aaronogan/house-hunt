from model.realestatelisting import RealEstateListing

data = {
    "list_date": "2020-10-24T023:01:38Z",
    "list_price": 230000,
    "listing_id": "1212",
    "property_id": "1234",
    "status": "for_sale",
}

def test_parse_list_date():
    listing = RealEstateListing(data)

    assert data['list_date'] == listing.list_date

def test_parse_list_price():
    listing = RealEstateListing(data)

    assert data['list_price'] == listing.list_price

def test_parse_listing_id():
    listing = RealEstateListing(data)

    assert data['listing_id'] == listing.listing_id

def test_parse_property_id():
    listing = RealEstateListing(data)

    assert data['property_id'] == listing.property_id

def test_parse_status():
    listing = RealEstateListing(data)

    assert data['status'] == listing.status

