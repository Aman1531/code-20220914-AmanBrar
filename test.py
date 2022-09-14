#!/usr/bin/env python3
import unittest


from bmi import bmi

class BmiTests(unittest.TestCase):
    def test_init_ok(self):
        bm = bmi("Male", 23,140)
        self.assertEqual(bm.gender, "Male")
        self.assertEqual(bm.weight, 23)
        self.assertEqual(bm.height,140)
        self.assertEqual(bm.bmi,round(23/(140/100)**2,2))

    def test_init_bad_gender(self):
        with self.assertRaises(TypeError):
            bm = bmi(1,23,140)

    def test_init_bad_weight_Height(self):
        with self.assertRaises(ValueError):
            bm = bmi("Male",0,12)
        with self.assertRaises(ValueError):
            bm = bmi("Male",100,0)




#bm = bmi("Male",23,14)
#print(bm.__dict__)
