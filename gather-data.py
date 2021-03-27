import yaml
import pyspark
from pathlib import Path
from model.rapidapi import RapidApi

config_path = Path(__file__).parent / "config.yml"
saved_search = {
    "city": "Denver",
    "state_code": "CO",
    "offset": 0,
    "limit": 200,
    "beds_min": 4,
    "baths_min": 2,
}

def get_config():
    with open(config_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as ex:
            print(ex)
            return None


if __name__ == "__main__":
    config = get_config()
    realtor_com_config = config['apis']['rapidapi']['realtor-com-real-estate']
    rapid_api = RapidApi(realtor_com_config)

    response = rapid_api.http_get('for-sale', saved_search)
    print(response)

