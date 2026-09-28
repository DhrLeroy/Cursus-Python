import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "4.0|--|5.5--6.5--7.0|--|8.0","10", "4", "5", "5.5", "6", "6", "6.5", "7", "7", "7.5", "8", "8", "9", "9.5", "10")

test_output(oefening_path, "-3.0|--|-1.5--25.0--25.0|--|43.0","7", "-3", "-1.5", "0", "25", "40", "41", "43")
