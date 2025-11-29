import json


def reformat(file):
    with open(file, "r") as f:
        d = json.load(f)

