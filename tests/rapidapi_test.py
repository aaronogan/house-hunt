from model.rapidapi import RapidApi

def test_get_endpoint_url_empty_endpoint_name():
    config = {
            "base-url": "endpoint-url/"
    }

    api = RapidApi(config)
    endpoint_url = api.get_endpoint_url()

    assert "endpoint-url/" == endpoint_url

def test_get_endpoint_url_with_endpoint_name():
    config = {
            "base-url": "endpoint-url/"
    }

    api = RapidApi(config)
    endpoint_url = api.get_endpoint_url("listings")

    assert "endpoint-url/listings" == endpoint_url

def test_get_headers():
    config = {
            "headers": {
                "x-rapidapi-key": "api-key",
                "x-rapidapi-host": "api-host"
            }
    }

    api = RapidApi(config)
    headers = api.get_headers()

    assert config['headers'] == headers

