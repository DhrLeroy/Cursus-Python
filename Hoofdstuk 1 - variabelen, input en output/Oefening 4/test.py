import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: Output checken...")
test_output(oefening_path, "John speelt graag The Last of Us!", "John", "The Last of Us")
print("Test 2: Output checken...")
test_output(oefening_path, "Elly speelt graag Tetris!", "Elly", "Tetris")