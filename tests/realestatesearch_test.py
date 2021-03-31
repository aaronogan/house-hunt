from model.realestatesearch import RealEstateSearchBuilder

def test_get_search_params_city():
    search = RealEstateSearchBuilder() \
        .set_city("Denver") \
        .build()

    assert "Denver" == search.to_json()['city']

def test_get_search_params_state():
    search = RealEstateSearchBuilder() \
        .set_state("CO") \
        .build()

    assert "CO" == search.to_json()['state']

def test_get_search_params_skip():
    search = RealEstateSearchBuilder() \
        .set_skip(9) \
        .build()

    assert 9 == search.to_json()['offset']

def test_get_search_params_take():
    search = RealEstateSearchBuilder() \
        .set_take(3) \
        .build()

    assert 3 == search.to_json()['limit']

def test_set_search():
    saved_search = {
        "city": "Denver",
        "state": "CO",
        "offset": 9,
        "limit": 3,
        "beds_min": 4,
        "baths_min": 2,
    }

    search = RealEstateSearchBuilder() \
        .set_search(saved_search) \
        .build()

    assert saved_search == search.to_json()

