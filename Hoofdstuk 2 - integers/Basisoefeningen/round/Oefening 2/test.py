import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: getal = 5")
test_output(oefening_path, "0", "5")


print("Test 2: getal = 10")
test_output(oefening_path, "10", "10")


print("Test 3: getal = 138")
test_output(oefening_path, "140", "138")


print("Test 4: getal = 2345")
test_output(oefening_path, "2340", "2345")

print("Test 5: getal = 2344")
test_output(oefening_path, "2340", "2344")

print("Test 6: getal = 2346")
test_output(oefening_path, "2350", "2346")
