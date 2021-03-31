import json
import yaml
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, lit
from model.realtorrealestateapi import RealtorRealEstateApi
from model.realestatesearch import RealEstateSearch

config_path = Path(__file__).parent / "config.yml"
arg_parser = ArgumentParser()
arg_parser.add_argument("-f", "--file", required=True, help="File in which API results are cached.")
arg_parser.add_argument("-l", "--local-only", action='store_true', help="Don't call the remote API, just use the source file (requires use of --file).")

saved_search = RealEstateSearch({
    "city": "Denver",
    "state_code": "CO",
    "offset": 0,
    "limit": 200,
    "beds_min": 4,
    "baths_min": 2,
})

def get_config():
    with open(config_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as ex:
            print(ex)
            return None

def write_dummy_json(file_path, json_data):
    with open(file_path, 'w') as output_file:
        json.dump(json_data, output_file)

def get_from_api():
    config = get_config()
    realtor_com_config = config['apis']['rapidapi']['realtor-com-real-estate']
    realtor_api = RealtorRealEstateApi(realtor_com_config)

    return realtor_api.http_get_listings(saved_search)


if __name__ == "__main__":
    args = vars(arg_parser.parse_args())

    spark = SparkSession \
            .builder \
            .appName("house-hunt") \
            .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/") \
            .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
            .getOrCreate()
    sc = spark.sparkContext

    if (args['local_only'] == False):
        response = get_from_api()
        write_dummy_json(args['file'], response)

    for_sale = spark.read.json(args['file']) \
            .select("data") \
            .withColumn("results", explode("data.results")) \
            .withColumn("created", lit(datetime.utcnow().replace(microsecond=0).isoformat()))

    select_columns = [
            "results.listing_id",
            "results.property_id",

            "results.status",
            "results.list_date",
            "results.last_update_date",
            "results.list_price",

            "results.description.type",
            "results.description.sub_type",
            "results.description.year_built",
            "results.description.beds",
            "results.description.baths",
            "results.description.sqft",
            "results.description.stories",
            "results.description.garage",

            "results.location.address.line",
            "results.location.address.city",
            "results.location.address.state_code",
            "results.location.county.name",
            "results.location.address.postal_code",
            "results.location.address.coordinate.lat",
            "results.location.address.coordinate.lon",

            "results.primary_photo.href",
            "results.permalink",

            "results.community",
            "results.description.sold_price",
            "created",
    ]
    for_sale = for_sale.select(select_columns)

    for_sale.write.format("com.mongodb.spark.sql") \
            .mode("append") \
            .option("database", "house-hunt") \
            .option("collection", "for_sale") \
            .save()

    print(for_sale.show(10, False))

