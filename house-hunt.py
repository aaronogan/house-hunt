import yaml
from rapidapi import RealtorFreeRealEstateApi

def get_config():
    file_name = "config.yml"
    with open(file_name, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as ex:
                print(ex)
                return None

if __name__ == "__main__":
    config = get_config()

    realtor_free_config = config['apis']['rapidapi']['realtor-free']
    realtor_api = RealtorFreeRealEstateApi(realtor_free_config)

    print(realtor_api.get_listings())

