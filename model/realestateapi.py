from abc import ABC, abstractmethod

class RealEstateApi:
    def __init__(self):
        pass

    @abstractmethod
    def get_listings(self):
        raise NotImplementedError


