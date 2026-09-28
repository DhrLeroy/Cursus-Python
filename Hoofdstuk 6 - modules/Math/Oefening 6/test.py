import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]", "2")

test_output(oefening_path, "-5\n-10\n-15\n-20\n-25\n-30\n-35\n-40\n-45\n-50\n[25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]", "-5")
