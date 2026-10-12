import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output, test_output_message

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output_message(oefening_path, "80 seconden", "0 uur 1 minuten en 20 seconden.", "80")

test_output_message(oefening_path, "100 seconden", "0 uur 1 minuten en 40 seconden.", "100")

test_output_message(oefening_path, "123456 seconden", "34 uur 17 minuten en 36 seconden.", "123456")
