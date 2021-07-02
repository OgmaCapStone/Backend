from app.utils.users_formating import user_format

import random
from faker import Faker

fake = Faker()

name = fake.name()
username = name + f"{random.randint(0,9)}"
username = username.replace(" ","")
email = username + "@gmail.com"

user = [
    name,
    email,
    username,
    [],
    [],
    "",
    "pass"
]

def test_should_pass():
    assert user_format(user) == {"name": name, "email": email, "username": username, "badges": [], "prefered_technologies": [], "profile_pic": "", "password": "pass"}

def test_should_not_pass():
    assert user_format(user) != {"email": email, "username": username, "badges": [], "prefered_technologies": [], "profile_pic": "", "password": "pass"}