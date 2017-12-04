# test_get_request.py
# Author: Cameron Smith

import pytest
import requests
import json
from test.utils import gen_profiles


def test_profileHandler_current_year(testing_server):

    expected_data = {
        "wwuid": "919428746",
        "minors": "Space Exploration, Awesomness",
        "office": "None",
        "photo": "profiles/1718/00958-2019687.jpg",
        "updated_at": "2017-10-10 00:05:26.384599",
        "class_of": "2014",
        "quote_author": "",
        "full_name": "Ryan Rabello",
        "hobbies": "",
        "relationship_status": "Will Date For Coffee",
        "majors": "Computer Engineering,",
        "favorite_books": "",
        "favorite_movies": "",
        "class_standing": "Senior",
        "graduate": "I sure hope so",
        "website": "",
        "department": "None",
        "high_school": "",
        "email": "ryan.rabello@wallawalla.edu",
        "favorite_music": "",
        "personality": "",
        "username": "ryan.rabello",
        "quote": "",
        "preprofessional": "",
        "career_goals": "",
        "phone": "",
        "birthday": "2-5",
        "favorite_food": "",
        "attached_to": "",
        "pet_peeves": "",
        "gender": "Male",
        "privacy": "0",
        "office_hours": "None"
     }

    url = "http://127.0.0.1:8888/profile/1718/ryan.rabello"
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)


## Define gen_profiles generator function in utils.py

def test_profileHandler_archive(testing_server):

    expected_data =
