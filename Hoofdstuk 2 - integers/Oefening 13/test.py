import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output, test_output_message

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output_message(oefening_path, "20 appels en 18 trossen druiven", "Je hebt 5 kistjes nodig.\nJe hebt nog een zakje nodig voor 1.3 kg fruit.", "20", "18")

test_output_message(oefening_path, "1 tros druiven", "Je hebt 0 kistjes nodig.\nJe hebt nog een zakje nodig voor 0.6 kg fruit.", "0", "1")

test_output_message(oefening_path, "1 appel", "Je hebt 0 kistjes nodig.\nJe hebt nog een zakje nodig voor 0.15 kg fruit.", "1", "0")