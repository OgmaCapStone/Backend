from typing import List


def user_format(user):
    json = dict()
    json["name"] = user[0]
    json["email"] = user[1]
    json["username"] = user[2]
    if user[3] != None:
        json["badges"] = user[3]
    else:
        json["badges"] = list()
    if user[4] != None:
        json["prefered_technologies"] = user[4]
    else:
        json["prefered_technologies"] = list()
    json["profile_pic"] = user[5]
    return json
