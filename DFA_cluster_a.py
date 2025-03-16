# DFA IMPLEMENTATION FOR "STARTS WITH CLUMP OF 'a'"

# TRANSITION TABLE: Rows = States, Columns = [‘a’, ‘b’]
transition_table = [
    [1, 3],  # State 0 → (a → 1, b → 3)
    [2, 3],  # State 1 → (a → 2, b → 3)
    [2, 2],  # State 2 → (a → 2, b → 2)
    [3, 3]   # State 3 → (Dead state )
]

# FINAL/ ACCEPTING STATE
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
