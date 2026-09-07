import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test: lepel")
test_output(oefening_path, "'lepel' is een palindroom.", "lepel")

print("Test: auto")
test_output(oefening_path, "'auto' is geen palindroom.", "auto")

print("Test: meetsysteem")
test_output(oefening_path, "'meetsysteem' is een palindroom.", "meetsysteem")



#test_output(oefening_path, "")
