#!/usr/bin/env python3


import json
from bmi import bmi

def get_data():
    with open("input.txt", "r") as f:
        return json.load(f)


if __name__ == '__main__':
    bmi_data = []
    data = get_data()
    for d in data:
        bmi_data.append(bmi(d["Gender"],d["WeightKg"],d["HeightCm"]))

    for bm in bmi_data:
        print(json.dumps(bm.__dict__))

    overweight=[ow for ow in bmi_data if "Over" in ow.bmi_category or "obese" in ow.bmi_category]
    print('\n\n',len(overweight), "people are overweight\n")
