import re

def validate_variable(var):
    pattern = r"^[a-zA-Z_][_ld]*$"  
    return bool(re.match(pattern, var))

# Test Cases
variables = ["_car", "name2", "x_", "a-l", "var-ld", "-invalid", "123hi", "_"]

for var in variables:
    if validate_variable(var):
        print(var, "-> Valid")
    else:
        print(var, "-> Invalid")
