import logging
import os
from datetime import date, timedelta

import awswrangler as wr
import boto3
import pandas as pd
import requests
from airflow.models import Variable


def main_request(page_number=1):
    """
    Function to make a request to the Guardian API and handle pagination.
    :return: The response in JSON format.
    """

    baseurl = "https://content.guardianapis.com"
    searchword = "/search?q=Nigeria"
    from_date = f"&from-date={date.today()}"
    to_date = f"&to-date={date.today()+timedelta(days=1)}"
    key = f"&api-key={Variable.get("SECRET_API_KEY")}"
    endpoint = baseurl+searchword+from_date+to_date+key

    response = requests.get(endpoint + f"&page={page_number}")
    if response.status_code == 200:
        logging.info("Request was successful")
        r = response.json()
        return r
    else:
        logging.error(f"Error: {r.status_code} - {r.text}")
        return None


def get_pages():
    """
    Function to get the number of pages from guardian API in JSON format
    :param json_response: The request response in JSON format.
    :return: The number of pages in the main request response
    """
    json_response = main_request()
    if json_response["response"]["pages"]:
        return json_response["response"]["pages"]
    else:
        logging.error("No pages found in the response.")
        return 0


def extract_page_articles(json_response):
    """
    Function to parse the JSON response and extract relevant information.
    :param json_response: The request response in JSON format.
    :return: A list of dictionaries containing the parsed data.
    """
    # json_response = main_request()
    return json_response["response"]["results"]


def to_dataframe():
    """
    Function to convert the list of dictionaries to a pandas DataFrame.
    :return: A pandas DataFrame containing the data.
    """
    pages = get_pages()
    articles_list = []
    for page in range(1, pages + 1):
        page_json = main_request(page_number=page)
        one_page_response = extract_page_articles(page_json)
        for article in one_page_response:
            articles_list.append(article)
    return pd.DataFrame(articles_list)


def boto_session():
    """
    Function to create a boto3 session.
    :return: A boto3 session object.
    """

    session = boto3.Session(
        aws_access_key_id=Variable.get("AWS_KEY_ID"),
        aws_secret_access_key=Variable.get("AWS_SECRET_KEY"),
        region_name="eu-central-1",
        aws_account_id=Variable.get("AWS_ACCOUNT_ID")
    )
    return session


def to_s3():
    """
    Function to write DataFrame to S3 in parquet and csv formats.
    :return: None
    """

    my_path = "s3://the-guardian-articles"
    wr.s3.to_parquet(
        df=to_dataframe(),
        path=f"{my_path}/nigeria-news:parquet",
        boto3_session=boto_session(),
        mode="append",
        dataset=True,
        filename_prefix="nigerian-news"
    )

    wr.s3.to_csv(
        df=to_dataframe(),
        path=f"{my_path}/nigeria-news:csv",
        boto3_session=boto_session(),
        mode="append",
        dataset=True,
        filename_prefix="nigerian-news"
    )


def complete_etl():
    main_request()
    get_pages()
    extract_page_articles()
    to_dataframe()
    to_s3()
    return "successful!"
