import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test: -1")
test_output(oefening_path, "Het getal moet strikt positief zijn.", "-1")

print("Test: 0")
test_output(oefening_path, "Het getal moet strikt positief zijn.", "0")

print("Test: 1")
test_output(oefening_path, "[]", "1")

1: []
2: [1]
3: [10, 5, 16, 8, 4, 2, 1]
4: [2, 1]
5: [16, 8, 4, 2, 1]