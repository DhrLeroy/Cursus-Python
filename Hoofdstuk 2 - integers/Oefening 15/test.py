import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output, test_output_message

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output_message(oefening_path, "80 meter in 23,7 seconden", "Je liep 12.15 km/u.", "80", "23.7")

test_output_message(oefening_path, "100 meter in 10 seconden", "Je liep 28.8 km/u.", "100", "10")

test_output_message(oefening_path, "200 meter in 83,5 seconden", "Je liep 3.45 km/u.", "200", "83.5")
