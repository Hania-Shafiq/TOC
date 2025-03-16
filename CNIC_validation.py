import re

def validate_cnic(cnic):
    pattern = r"^[1-7]\d{4}-\d{7}-\d$" 
    return bool(re.match(pattern, cnic))

# Test Cases
cnics = ["42101-1234567-8", "12345-6789012-3", "82101-1234567-8", "72101-1234567-0", "00321-1234567-9"]

for cnic in cnics:
    is_valid = validate_cnic(cnic)
    
    if is_valid:
        print(cnic, "-> Valid")
    else:
        print(cnic, "-> Invalid")
