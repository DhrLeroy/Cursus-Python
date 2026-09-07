import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test: APPEL")
test_output(oefening_path, "A\nAP\nAPP\nAPPE]\nAPPEL]","APPEL")

print("Test: BANAAN")
test_output(oefening_path, "B\nBA\nBAN\nBANA]\nBANAA\nBANAAN]","BANAAN")



#test_output(oefening_path, "")
