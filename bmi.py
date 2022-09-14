#!/usr/bin/env python3

bmi_ranges = [{(0,18.4):"Underweight,Malnutrition risk"},
              {(18.5,24.9):"Normal weight,Low risk"},
              {(25,29.9):"Over weight,Enhanced risk"},
              {(30,34.9):"Moderately obese,Medium risk"},
              {(35,39.9):"Severly obese,High risk"},
              {(40,10000):"Very severly obese,Very high risk"}]

class bmi:
    def __init__(self,gender,weight,height):
        if not isinstance(gender,str):
            raise TypeError("gender should be a string")
        if height <= 0 or weight <=0:
            raise ValueError("Weight/Height can not be zero or -ve")
        self.gender=gender
        self.weight = weight
        self.height = height
        self.bmi = round(weight/(height/100) ** 2,2)
        self.bmi_category = ""
        self.health_risk = ""
        for br in bmi_ranges:
            bi = round(self.bmi,1)
            br = list(br.items())
            cat = br[0][1].split(',')
            r = br[0][0]
            if r[0] <= bi <= r[1]:
                self.bmi_category = cat[0]
                self.health_risk = cat[1]
                break


