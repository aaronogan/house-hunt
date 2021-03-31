from model.realestatesearch import RealEstateSearch

def test_get_search_params_city():
    search = RealEstateSearch() \
        .set_city("Denver") \
        .get()

    assert "Denver" == search['city']

def test_get_search_params_state():
    search = RealEstateSearch() \
        .set_state("CO") \
        .get()

    assert "CO" == search['state']

def test_get_search_params_skip():
    search = RealEstateSearch() \
        .set_skip(9) \
        .get()

    # api expects string, not a typo
    assert "9" == search['skip']

def test_get_search_params_take():
    search = RealEstateSearch() \
        .set_take(3) \
        .get()

    # api expects string, not a typo
    assert "3" == search['take']

