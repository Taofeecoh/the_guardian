import os

import awswrangler as wr
import boto3
import pandas as pd
from dotenv import load_dotenv

import guardianmodule as gm

load_dotenv()
key = os.getenv("GUARDIAN_KEY")
endpoint = "https://content.guardianapis.com"
queries = f"/search?q=Nigeria&from-date=2025-01-01&api-key={key}"

base_request = gm.main_request(endpoint, queries)
page_size = gm.get_pages(base_request)

articles_list = []
for page in range(1, page_size + 1):
    page_json = gm.main_request(endpoint, queries, page_number=page)
    one_page_response = gm.extract_page_articles(page_json)
    for article in one_page_response:
        articles_list.append(article)

df = pd.DataFrame(articles_list)
df.to_csv("guardian_NigerianArticles.csv", index=False)

session = boto3.Session(
    aws_access_key_id=os.getenv("ID"),
    aws_secret_access_key=os.getenv("KEY")
)

my_path = "s3://taofeecoh-bucket"
wr.s3.to_parquet(
    df=df,
    path=f"{my_path}/app4/nigerian-guardian:v1",
    boto3_session=session,
    mode="append",
    dataset=True
    )
