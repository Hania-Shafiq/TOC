# DFA IMPLEMENTATION FOR "aa(a+b)*"
# TRANSITION TABLE: Rows = States, Columns = ['a', 'b']
transition_table = [
    [1, 3],  # State q0 → (a → q1, b → q3)
    [2, 3],  # State q1 → (a → q2, b → q3)
    [2, 2],  # State q2 → (a → q2, b → q2)
    [3, 3]   # State q3 → Dead state (always stays in q3)
]
# FINAL / ACCEPTING STATE
final_state = 2

def is_accepted(input_string):
    state = 0  # Initial State
    for char in input_string:
        if char == 'a':
            state = transition_table[state][0]  # Move on 'a'
        elif char == 'b':
            state = transition_table[state][1]  # Move on 'b'
        else:
            return "Invalid Input"  # Reject if input is not 'a' or 'b'
    
    return "Accepted" if state == final_state else "Rejected"

# TEST CASES
print(is_accepted("aaba"))  # Accepted
print(is_accepted("Gbaba"))  # Invalid Input
print(is_accepted("aaa"))   # Accepted
print(is_accepted("bbba"))  # Rejected
print(is_accepted("aaabbbaaa")) # Accepted
