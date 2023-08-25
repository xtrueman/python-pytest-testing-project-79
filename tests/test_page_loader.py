import os, os.path
import logging
import pytest
import page_loader

logging.getLogger("PIL").setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)


@pytest.fixture
def dir_for_tests(tmp_path):
    directory = tmp_path / "dir"
    directory.mkdir()
    return f"{tmp_path}/dir"


def test_url_to_filename():
    assert page_loader.url_to_filename('https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'
    assert page_loader.url_to_filename('https://mc.yandex.ru/metrika/tag.js', '.js') == 'mc-yandex-ru-metrika-tag-js.js'

def test_page_loader_check_return_string(dir_for_tests, requests_mock):
    tmp_path = dir_for_tests

    requests_mock.get("https://ru.hexlet.io/courses", text="data")
    file_path = page_loader.download("https://ru.hexlet.io/courses", tmp_path)

    assert file_path == f"{tmp_path}/ru-hexlet-io-courses.html"


def test_page_loader_check_requests_count(dir_for_tests, requests_mock):
    tmp_path = dir_for_tests

    requests_mock.get("https://some_page.com", text="data")
    page_loader.download("https://some_page.com", tmp_path)

    assert requests_mock.call_count == 1


def test_page_loader_download_page(dir_for_tests):
    tmp_path = dir_for_tests

    file_path = page_loader.download("https://ru.hexlet.io/courses", tmp_path)
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 1000
