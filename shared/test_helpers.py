import importlib.util
import sys
import os
from io import StringIO
from unittest.mock import patch

# Kleuren voor duidelijke feedback
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Interne flag, zodat de terminal maar één keer wordt gecleard per test-file
__terminal_cleared = False


def clear_terminal_once():
    """Leeg de terminal, maar slechts één keer per testbestand."""
    global __terminal_cleared
    if not __terminal_cleared:
        os.system('cls' if os.name == 'nt' else 'clear')
        __terminal_cleared = True



def load_module(path, inputs=None):
    """Laadt een oefening en vangt de stdout + input."""
    inputs = inputs or []

    spec = importlib.util.spec_from_file_location("oefening", path)
    oefening = importlib.util.module_from_spec(spec)

    with patch("builtins.input", side_effect=inputs), \
         patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        spec.loader.exec_module(oefening)

    return mock_stdout.getvalue().strip(), oefening


def test_output(oefening_path, expected_output, *inputs):
    clear_terminal_once()
    inputs = list(inputs)
    """Test of de uitvoer exact klopt."""
    actual_output, _ = load_module(oefening_path, inputs)

    if actual_output == expected_output:
        print(f"{GREEN}✅ Test geslaagd!{RESET}")
    else:
        print(f"{RED}❌ Test mislukt!{RESET}")
        print(f"  Verwachte uitvoer: '{expected_output}'")
        print(f"  Jouw uitvoer    : '{actual_output}'")


def test_variable(oefening_path, var_name, expected_value=None):
    """Test of een variabele bestaat en optioneel de waarde controleert."""
    _, oefening = load_module(oefening_path)

    if not hasattr(oefening, var_name):
        print(f"{RED}❌ Variabele '{var_name}' ontbreekt!{RESET}")
        return

    value = getattr(oefening, var_name)
    if expected_value is None or value == expected_value:
        print(f"{GREEN}✅ Variabele '{var_name}' is correct!{RESET}")
    else:
        print(f"{RED}❌ Variabele '{var_name}' heeft verkeerde waarde!{RESET}")
        print(f"  Verwacht: {expected_value}, Jouw waarde: {value}")
