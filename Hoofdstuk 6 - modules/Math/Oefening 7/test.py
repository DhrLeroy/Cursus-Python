import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "1. The Lord of the Rings: The Fellowship of the Ring\n2. The Lord of the Rings: The Two Towers\n3. The Lord of the Rings: The Return of the King", "3", "The Lord of the Rings: The Return of the King", "The Lord of the Rings: The Two Towers", "The Lord of the Rings: The Fellowship of the Ring")

