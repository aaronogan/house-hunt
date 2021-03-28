import json
import yaml
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
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
dummy_json_path = Path(__file__).parent / "for-sale.json"

def get_config():
    with open(config_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as ex:
            print(ex)
            return None

def write_dummy_json(json_data):
    with open(dummy_json_path, 'w') as output_file:
        json.dump(json_data, output_file)

def read_dummy_json():
    with open(dummy_json_path, 'r') as input_file:
        return json.load(input_file)

def get_from_api():
    config = get_config()
    realtor_com_config = config['apis']['rapidapi']['realtor-com-real-estate']
    rapid_api = RapidApi(realtor_com_config)

    return rapid_api.http_get('for-sale', saved_search)

def get_from_api_and_cache_locally():
    response = get_from_api()
    write_dummy_json(response)


if __name__ == "__main__":

    # currently reading from dummy json
    # TODO add command line options to control where we pull data from
    spark = SparkSession \
            .builder \
            .appName("house-hunt") \
            .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/listings.coll") \
            .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/listings.coll") \
            .getOrCreate()
    sc = spark.sparkContext


    for_sale = spark.read.json(str(dummy_json_path)) \
            .select("data") \
            .withColumn("results", explode("data.results")) \
            .select("results.community", "results.description.baths", "results.description.beds", "results.description.garage", "results.description.sqft", "results.description.sold_price", "results.description.stories", "results.description.type", "results.description.sub_type", "results.description.year_built", "results.list_date", "results.list_price", "results.listing_id", "results.location.address.coordinate.lat", "results.location.address.coordinate.lon", "results.location.address.line", "results.location.address.city", "results.location.address.state_code", "results.location.address.postal_code", "results.location.county.name", "results.property_id", "results.status", "results.primary_photo.href", "results.permalink", "results.last_update_date")
    print(for_sale.show(10, False))
    
