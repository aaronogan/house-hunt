from model.realestatesearch import RealEstateSearch

def test_get_search_params_city():
    search = RealEstateSearch()
    search.set_city("Denver")

    params = search.get_search_params()

    assert "Denver" == params['city']

def test_get_search_params_state():
    search = RealEstateSearch()
    search.set_state("CO")

    params = search.get_search_params()

    assert "CO" == params['state']

def test_get_search_params_skip():
    search = RealEstateSearch()
    search.set_skip(9)

    params = search.get_search_params()

    # api expects string, not a typo
    assert "9" == params['skip']

def test_get_search_params_take():
    search = RealEstateSearch()
    search.set_take(3)

    params = search.get_search_params()

    # api expects string, not a typo
    assert "3" == params['take']

