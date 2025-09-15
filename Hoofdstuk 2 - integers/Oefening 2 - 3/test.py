import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "x^5 - x^4 met x = 2 is 16", "2")

print("Test 2: x = 3")
test_output(oefening_path, "x^5 - x^4 met x = 3 is 162", "3")
