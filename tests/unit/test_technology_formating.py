import app.utils.technologies_formating as tf

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
    assert tf.technologies_formating(user) == {"name": name, "email": email, "username": username, "badges": [], "prefered_technologies": [], "profile_pic": ""}

def test_should_not_pass():
    assert tf.technologies_formating(user) == {"email": email, "username": username, "badges": [], "prefered_technologies": [], "profile_pic": ""}