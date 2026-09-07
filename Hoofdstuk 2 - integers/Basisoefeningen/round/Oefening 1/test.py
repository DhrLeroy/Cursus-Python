import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: a = 5, b = 6")
test_output(oefening_path, "0.83", "5", "6")


print("Test 1: a = 0, b = 1")
test_output(oefening_path, "0.0", "0", "1"  )


print("Test 1: a = -2, b = 1")
test_output(oefening_path, "-2.0", "-2", "1")

print("Test 1: a = 100, b = 3")
test_output(oefening_path, "33.33", "100", "3")
