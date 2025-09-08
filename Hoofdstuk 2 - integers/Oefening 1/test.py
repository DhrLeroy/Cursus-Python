import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: a = 9, b = 2")
test_output(oefening_path, "som = 11\nverschil = 7\nproduct = 18\nquotiënt = 4.5\nmacht = 81\nwortel = 3.0", "9", "2")

print("Test 2: a = 5, b = 3")
test_output(oefening_path, "som = 8\nverschil = 2\nproduct = 15\nquotiënt = 1.6666666666666667\nmacht = 125\nwortel = 1.7099759466766968", "5", "3")
