import os
from datetime import date, timedelta

import awswrangler as wr
import boto3
import pandas as pd
from dotenv import load_dotenv

import guardianmodule as gm

load_dotenv()

baseurl = "https://content.guardianapis.com"
searchword = "/search?q=Nigeria"
from_date = f"&from-date={date.today()}"
to_date = f"&to-date={date.today()+timedelta(days=1)}"
key = f"&api-key={os.getenv("GUARDIAN_KEY")}"

endpoint = baseurl+searchword+from_date+to_date+key

request = gm.main_request(endpoint)
pages = gm.get_pages(request)

articles_list = []
for page in range(1, pages + 1):
    page_json = gm.main_request(endpoint, page_number=page)
    one_page_response = gm.extract_page_articles(page_json)
    for article in one_page_response:
        articles_list.append(article)

df = pd.DataFrame(articles_list)

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name="eu-central-1",
    aws_account_id=os.getenv("AWS_ACCOUNT_ID")
)

my_path = "s3://the-guardian-articles"
wr.s3.to_parquet(
    df=df,
    path=f"{my_path}/nigerian-news:v1",
    boto3_session=session,
    mode="append",
    dataset=True,
    filename_prefix="nigerian-news"
    )

wr.s3.to_csv(
    df=df,
    path=f"{my_path}/nigerian-news:v2",
    boto3_session=session,
    mode="append",
    dataset=True,
    filename_prefix="nigerian-news"
    )

