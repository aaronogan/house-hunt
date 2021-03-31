
class RealEstateSearch:
    def __init__(self):
        self.city = None
        self.state = None
        self.skip = None
        self.take = None

    def set_city(self, city):
        self.city = city
        return self

    def set_state(self, state_postal_code):
        self.state = state_postal_code
        return self

    def set_skip(self, skip):
        self.skip = skip
        return self

    def set_take(self, take):
        self.take = take
        return self

    def get(self):
        params = {}

        if (self.city != None):
            params['city'] = self.city

        if (self.state != None):
            params['state'] = self.state

        if (self.skip != None):
            params['skip'] = str(self.skip)

        if (self.take != None):
            params['take'] = str(self.take)

        return params

