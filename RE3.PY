# DFA IMPLEMENTATION FOR "Even number of a's and odd number of b's"

# TRANSITION TABLE: Rows = States, Columns = ['a', 'b']
transition_table = [
    [1, 2],  # State q0 → (a → q1, b → q2)
    [0, 3],  # State q1 → (a → q0, b → q3)
    [3, 0],  # State q2 → (a → q3, b → q0)
    [2, 1]   # State q3 → (a → q2, b → q1)
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
print(is_accepted("aab"))  # Accepted
print(is_accepted("abab")) # Rejected
print(is_accepted("bbba")) # Accepted
print(is_accepted("aaa"))  # Rejected
print(is_accepted("bbaa")) # Accepted





