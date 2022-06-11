import json

with open('helpers/api.json', 'r') as file:
    py_obj = json.load(file)


def creation_of_user():
    """Parse py_obj and return a dict for api request to create user."""
    return py_obj[0]


def creation_of_pet():
    """Parse py_obj and return a dict for api request to create pet."""
    return py_obj[1]


def update_pet_name():
    """Parse py_obj and return a dict for api request to rename pet."""
    return py_obj[2]
