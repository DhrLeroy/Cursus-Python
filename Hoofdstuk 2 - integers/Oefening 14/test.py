import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output, test_output_message

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output_message(oefening_path, "6 procent op 7 jaar", "Totaalbedrag na 7 jaar: 152.04", "6", "7")

test_output_message(oefening_path, "4.5 procent op 10 jaar", "Totaalbedrag na 10 jaar: 156.7", "4.5", "10")

test_output_message(oefening_path, "0.01 procent op 100 jaar", "Totaalbedrag na 100 jaar: 101.01", "0.01", "100")
