
class RealEstateListing:
    properties = [
            "list_date",
            "list_price",
            "listing_id",
            "property_id",
            "status"
    ]

    def __init__(self, data):
        for prop in self.properties:
            self.__dict__[prop] = data[prop]

