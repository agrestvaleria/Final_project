import json

with open('/home/valerya/PycharmProjects/Final_project/helpers/api.json',
          'r') as file:
    py_obj = json.load(file)


def creation_of_user():
    return py_obj[0]


def creation_of_pet():
    return py_obj[1]


def update_pet_name():
    return py_obj[2]
