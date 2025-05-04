# DFA IMPLEMENTATION FOR "(ab+aa)(a+b)*"
# TRANSITION TABLE: Rows = States, Columns = ['a', 'b']
transition_table = [
    [1, 4],  # State q0 → (a → q1, b → q4)
    [2, 4],  # State q1 → (a → q2, b → q4)
    [2, 3],  # State q2 → (a → q2, b → q3)
    [3, 3],  # State q3 → Dead state
    [4, 4]   # State q4 → Dead state
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
print(is_accepted("ababa"))  # Accepted
print(is_accepted("aaaa"))   # Accepted
print(is_accepted("bab"))    # Rejected
print(is_accepted("aaabb"))  # Accepted
print(is_accepted("baba"))   # Rejected
