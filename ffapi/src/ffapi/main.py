from typing import Union
import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()
df=pd.read_parquet("/home/esthercho/code/ffapi/data") # --> 전역 변수로 선언 시 성능 향상

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sample")
def sample(movie_code: int):
    sample_df=df.sample(n=5) # --> sample은 pandas에 내장된 함수
    r=sample_df.to_dict(orient='records') # to_dict()는 dictionary 형태로 만들어주는 함수
    return r

@app.get("/movie/{movie_code}")
def movie_meta(movie_code: str):
    meta_df=df[df['movieCd']==movie_code]
    if meta_df.empty:
        raise HTTPException(status_code=404, detail="그런 영화 없습니다.")
    r=meta_df.iloc[0].to_dict()
    return r
