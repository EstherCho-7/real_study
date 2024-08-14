from mdata.ml import save_movies

def test_save_movies():
    r=save_movies(year=2015, sleep_time=0.1)
    assert r
