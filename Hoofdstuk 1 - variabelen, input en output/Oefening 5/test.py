import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")


test_output(oefening_path, 'Mijn favoriete quote: "Roads? Where we\'re going, we don\'t need roads"', "Roads? Where we're going, we don't need roads")

test_output(oefening_path, 'Mijn favoriete quote: "For Frodo"', "For Frodo")