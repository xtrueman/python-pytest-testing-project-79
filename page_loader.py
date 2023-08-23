#!python3

import os
import sys
import logging
import argparse
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


def make_parser():
    parser = argparse.ArgumentParser(
        prog="page-loader",
        description="web page downloader")

    parser.add_argument(
        "url",
        type=str,
    )

    help_ = f"output directory, default is current ('{os.getcwd()}')"
    parser.add_argument(
        "-o",
        "--output",
        default=os.getcwd(),
        help=help_,
        type=str,
    )
    return parser


parser = make_parser()
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(0)

args = parser.parse_args()
try:
    path = download(args.url, args.output)
    absolute_path = os.path.abspath(path)
    print(f"Page was downloaded as '{absolute_path}'")
except Exception as error:
    logging.error(error)
    sys.exit(1)
