# test_get_request.py
# Author: Cameron Smith

import pytest
import requests
import json

def test_good_request(testing_server):

    url = "http://127.0.0.1:8888/search/all"
    resp = requests.get(url)
    assert (resp.status_code == 200)

def test_good_request_data(testing_server):
    null = None
    expected_data = {
        "username": "ryan.rabello",
        "wwuid": "919428746",
        "roles": "",
        "photo": "profiles/1718/00958-2019687.jpg",
        "status": null,
        "full_name": "Ryan Rabello",
        }

    url = "http://127.0.0.1:8888"
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)

def test_nonexistent_page(testing_server):

    url = "http://127.0.0.1:8888/nonexistent"
    resp = requests.get(url)
    assert (resp.status_code == 404)
