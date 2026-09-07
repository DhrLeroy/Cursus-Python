import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: a = 1.2345, b = 2.3456")
test_output(oefening_path, "2.8956", "1.2345", "2.3456")

print("Test 2: a = 0, b = 0")
test_output(oefening_path, "0.0", "0", "0")


print("Test 3: a = -2.9863455, b = 3.980384")
test_output(oefening_path, "-11.8868", "-2.9863455", "3.980384")

print("Test 4: a = 9.876543210, b = 1.23456789")
test_output(oefening_path, "12.1933", "9.876543210", "1.23456789")