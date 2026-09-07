import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "[1, 2, 3, 4, 5, 6]\n[1, 2, 3]\n[3, 4, 5, 6]\n[2, 4, 6]\n[6, 5, 4, 3, 2, 1]","6")

test_output(oefening_path, "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3]\n[7, 8, 9, 10]\n[2, 4, 6, 8, 10]\n[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]","10")


#test_output(oefening_path, "")
