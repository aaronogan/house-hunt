class RealEstateSearch:
    def __init__(self, search_json={}):
        self.search_dict = dict(search_json)

    def to_json(self):
        return self.search_dict


class RealEstateSearchBuilder:

    def __init__(self):
        self.dict = dict({})

    def __getitem__(self, key):
        if (key not in self.dict):
            raise KeyError
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def set_search(self, search_json):
        self.dict = dict(search_json)
        return self

    def set_city(self, city):
        self.dict['city'] = city
        return self

    def set_state(self, state_postal_code):
        self.dict['state'] = state_postal_code
        return self

    def set_skip(self, skip):
        self.dict['offset'] = skip
        return self

    def set_take(self, take):
        self.dict['limit'] = take
        return self

    def build(self):
        return RealEstateSearch(self.dict)

