import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")


print("Test 1: Geldig telefoonnummer met prefix 00324")
test_output(oefening_path, "***********34", "0032412345634")

print("Test 2: Geldig telefoonnummer met prefix 04")
test_output(oefening_path, "********34", "0412345634")

print("Test 3: Geldig telefoonnummer met prefix +324")
test_output(oefening_path, "**********34", "+32412345634")

print("Test 4: Geldig nummer met andere laatste cijfers")
test_output(oefening_path, "***********99", "0032412345699")

print("Test 5: Geldig nummer met andere laatste cijfers")
test_output(oefening_path, "********71", "0412345671")

print("Test 6: Geldig nummer met andere laatste cijfers")
test_output(oefening_path, "**********78", "+32412345678")

print("Test 7: Geldig nummer met prefix 00324 en andere cijfers")
test_output(oefening_path, "***********34", "0032498765634")

print("Test 8: Geldig nummer met prefix 04 en andere cijfers")
test_output(oefening_path, "********34", "0498765634")

print("Test 9: Geldig nummer met prefix +324 en andere cijfers")
test_output(oefening_path, "**********34", "+32498765634")


print("Test 10: Ongeldige prefix 0033")
test_output(oefening_path, "Ongeldig telefoonnummer", "00331412345634")

print("Test 11: Ongeldige prefix 05")
test_output(oefening_path, "Ongeldig telefoonnummer", "05123456734")

print("Test 12: Ongeldige prefix +331")
test_output(oefening_path, "Ongeldig telefoonnummer", "+33123456734")

print("Test 13: Ongeldige prefix 0324")
test_output(oefening_path, "Ongeldig telefoonnummer", "0324123456734")

print("Test 14: Ongeldige prefix zonder 00 of +")
test_output(oefening_path, "Ongeldig telefoonnummer", "324123456734")

print("Test 15: Ongeldige buitenlandse prefix")
test_output(oefening_path, "Ongeldig telefoonnummer", "0049123456734")


print("Test 16: Eén cijfer te weinig bij prefix 00324")
test_output(oefening_path, "Ongeldig telefoonnummer", "003241234563")

print("Test 17: Eén cijfer te weinig bij prefix 04")
test_output(oefening_path, "Ongeldig telefoonnummer", "041234567")

print("Test 18: Eén cijfer te weinig bij prefix +324")
test_output(oefening_path, "Ongeldig telefoonnummer", "+3241234567")

print("Test 19: Alleen de prefix 00324")
test_output(oefening_path, "Ongeldig telefoonnummer", "00324")

print("Test 20: Alleen de prefix 04")
test_output(oefening_path, "Ongeldig telefoonnummer", "04")

print("Test 21: Alleen de prefix +324")
test_output(oefening_path, "Ongeldig telefoonnummer", "+324")


print("Test 22: Eén cijfer te veel bij prefix 00324")
test_output(oefening_path, "Ongeldig telefoonnummer", "00324123456734")

print("Test 23: Eén cijfer te veel bij prefix 04")
test_output(oefening_path, "Ongeldig telefoonnummer", "041234567834")

print("Test 24: Eén cijfer te veel bij prefix +324")
test_output(oefening_path, "Ongeldig telefoonnummer", "+3241234567834")

print("Test 25: Veel te veel cijfers bij prefix 00324")
test_output(oefening_path, "Ongeldig telefoonnummer", "003241234567890")

print("Test 26: Veel te veel cijfers bij prefix 04")
test_output(oefening_path, "Ongeldig telefoonnummer", "041234567890")

print("Test 27: Veel te veel cijfers bij prefix +324")
test_output(oefening_path, "Ongeldig telefoonnummer", "+3241234567890")


print("Test 31: Spatie na de prefix 00324")
test_output(oefening_path, "Ongeldig telefoonnummer", "00324 123456734")

print("Test 32: Spatie na de prefix 04")
test_output(oefening_path, "Ongeldig telefoonnummer", "04 123456734")

print("Test 33: Spatie na de prefix +324")
test_output(oefening_path, "Ongeldig telefoonnummer", "+324 123456734")

print("Test 34: Streepje in telefoonnummer met prefix 00324")
test_output(oefening_path, "Ongeldig telefoonnummer", "00324-123456734")

print("Test 35: Streepje in telefoonnummer met prefix 04")
test_output(oefening_path, "Ongeldig telefoonnummer", "04-123456734")

print("Test 36: Streepje in telefoonnummer met prefix +324")
test_output(oefening_path, "Ongeldig telefoonnummer", "+324-123456734")


print("Test 37: Lege invoer")
test_output(oefening_path, "Ongeldig telefoonnummer", "")

