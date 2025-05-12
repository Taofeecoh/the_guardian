import logging

import requests


def main_request(baseurl, parameter, page_number=1):
    """
    Function to make a request to the Guardian API and handle pagination.
    :param baseurl: The base URL of the API.
    :param parameter: The endpoint to get info about pagesizes for the request.
    :return: The response in JSON format.
    """
    response = requests.get(baseurl + parameter + f"&page={page_number}")
    if response.status_code == 200:
        logging.info("Request was successful")
        r = response.json()
        return r
    else:
        logging.error(f"Error: {r.status_code} - {r.text}")
        return None


def get_pages(json_response):
    """
    Function to get the number of pages from guardian API in JSON format
    :param json_response: The request response in JSON format.
    :return: The number of pages in the main request response
    """
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
    return json_response["response"]["results"]
