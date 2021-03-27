from abc import ABC, abstractmethod

class RealEstateApi:
    def __init__(self):
        pass

    @abstractmethod
    def http_get_listings(self, search):
        raise NotImplementedError

