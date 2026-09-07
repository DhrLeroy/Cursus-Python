import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: Lengte = 1.8, Gewicht = 74")
test_output(oefening_path, "BMI = 23", "1.8", "74")

print("Test 2: Lengte = 1.67, Gewicht = 65")
test_output(oefening_path, "BMI = 23", "1.67", "65")

print("Test 3: Lengte = 2.01, Gewicht = 120")
test_output(oefening_path, "BMI = 30", "2.01", "120")

print("Test 4: Lengte = 1.82, Gewicht = 55")
test_output(oefening_path, "BMI = 17", "1.82", "55")