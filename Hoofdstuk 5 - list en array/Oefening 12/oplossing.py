woord = input("Woord: ")
wel_geen = ""
if woord != woord[::-1]:
    wel_geen = "g"
print(f"'{woord}' is {wel_geen}een palindroom.")