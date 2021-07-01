import app.utils.users_formating as uf

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
    ""
]

def test_should_pass():
    assert uf.user_format(user) == {"name": name, "email": email, "username": username, "badges": [], "prefered_technologies": [], "profile_pic": ""}

def test_should_not_pass():
    assert uf.user_format(user) == {"email": email, "username": username, "badges": [], "prefered_technologies": [], "profile_pic": ""}