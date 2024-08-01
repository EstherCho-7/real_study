from study_movie.api.call import gen_url, req, get_key, req2list, list2df, save2df
import pandas as pd

def test_private_key():
    key=get_key
    assert key

def test_gen_url():
    url=gen_url()
    if "http" in url:
        print(url)
    else:
        print("nope")

def test_req():
    code, data=req()
    assert code==200

def test_dataframe():
    l=req2list(load_dt='20120101')
    assert len(l)>0

def test_list2df():
    df=list2df()
    assert isinstance(df, pd.DataFrame)

def test_save2df():
    df=save2df(load_dt='20120101')
    assert isinstance(df, pd.DataFrame)
