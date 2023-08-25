import os
import logging
import requests
from urllib.parse import urlparse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) \
            Gecko/20100101 Firefox/112.0"
}

logging.basicConfig(level=logging.INFO)

def url_to_filename(url: str, type=".html"):
    new_url = url.replace("https://", "").replace("http://", "")
    result = ""
    for char in new_url:
        if char.isalnum():
            result += char
        else:
            result += "-"

    return result + type

def download(url: str, path: str = os.getcwd()) -> str:
    logging.info(f"requested url: {url}")
    absoulute_path = os.path.abspath(path)
    logging.info(f"output path: {absoulute_path}")

    request = requests.get(
        url, headers=headers,
        allow_redirects=True, timeout=(3, 7)
    )

    logging.info(f"responce status: {request.status_code}")

    new_html_file_name = url_to_filename(url)
    new_html_path = os.path.join(path, new_html_file_name)

    new_html_absolute_path = os.path.abspath(new_html_path)
    logging.info(f"write html file: {new_html_absolute_path}")

    with open(new_html_absolute_path, "w") as html_file:
        html_file.write(request.text)

    return new_html_path
