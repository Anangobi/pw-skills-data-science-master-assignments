x = (1, 2, 3, 4)
try:
    print(x[10])
except LookupError as e:
    print(f"{e}, {e.__class__}")

x = "Pylenin"
try:
    print(x[10])
except LookupError as e:
    print(f"{e}, {e.__class__}")
