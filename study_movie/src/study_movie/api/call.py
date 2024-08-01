import requests  # for req
import os  # for get_key from os
import pandas as pd

def get_key():  #1
    """YOU MUST HAVE A KEY FOR ACCESS"""
    key=os.getenv("MOVIE_API_KEY")
    return key

def gen_url(load_dt='20120101'):  #2
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key=get_key()
    url=f"{base_url}?key={key}&targetDt={load_dt}"
    return url

def req(load_dt='20120101'):   #3, request by load_dt, default=''
    url=gen_url(load_dt)
    r=requests.get(url)
    code=r.status_code
    data=r.json()
    return code, data

def req2list(load_dt):   #4, request --> list
    _, data=req(load_dt)
    l=data['boxOfficeResult']['dailyBoxOfficeList']  # ==> [{'':''},{'':''}], boxOfficeResult > dailyBoxofficeList
    df=pd.DataFrame(l)
    return df

def list2df(load_dt='20120101'):   #5, list --> dataframe
    l=req2list(load_dt)
    df=pd.DataFrame(l)
    return df

def save2df(load_dt='20120101'):   #6, save!
    # point that airflow acts
    df=list2df(load_dt)
    df['load_dt']=load_dt
    return df
    
