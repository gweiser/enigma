"""Rotors"""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
reflector = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']
reflector_b = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

# all_rotors = [
#     ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'], # Turnover: Q
#     ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'], # Turnover: E
#     ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'], # Turnover: V
#     ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'], # Turnover: J
#     ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']  # Turnover: Z
# ]

# all_rotors = {
#     "rotor_one": ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'],
#     "rotor_two": ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'],
#     "rotor_three": ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'],
#     "rotor_four": ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'],
#     "rotor_five": ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
# }

all_rotors = [
    {
        "rotor": ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'],
        "turnover": "Q"
    },
    {
        "rotor": ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'],
        "turnover": "E"
    },
    {
        "rotor": ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'],
        "turnover": "V"
    },
    {
        "rotor": ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'],
        "turnover": "J"
    },
    {
        "rotor": ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K'],
        "turnover": "Z"
    }
]


def initialise_rotor_position(rotor, position):
    """Bring rotor into the desired starting position"""

    rotor = all_rotors[rotor]
    starting_letter_index = rotor.index(position)
    
    # Split list at starting letter, then append new list end (wrapping around)
    list_beginning = rotor[starting_letter_index:len(rotor)]
    list_end = rotor[0:starting_letter_index]
    new_rotor = list_beginning + list_end
 
    return new_rotor



def initialise_rotor_ring():
    # TODO
    """Bring rotor ring position into desired state"""
    ...
    #>> ?



def rotate_rotors():
    """Rotate the rotors (change order of letters in list)"""

    # If rotor 3 is not at its turnover position
    if rotor_3["rotor"][0] != rotor_3["turnover"]:
        # Just rotate rotor 3 --> "Rotate" rotor 3 by appending index 0 to end of list
        rotor_3["rotor"].append(rotor_3["rotor"][0])
        rotor_3["rotor"].pop(0)
    # If rotor 3 is at its turnover position
    elif rotor_3["rotor"][0] == rotor_3["turnover"]:
        # "Rotate" rotor 3 by appending index 0 to end of list
        rotor_3["rotor"].append(rotor_3["rotor"][0])
        rotor_3["rotor"].pop(0)
        # If rotor 2 is at its turnover position
        if rotor_2["rotor"][0] == rotor_2["turnover"]:
            # Rotate" rotor 1 by appending index 0 to end of list
            rotor_1["rotor"].append(rotor_1["rotor"][0])
            rotor_1["rotor"].pop(0)
        # Rotate" rotor 2 by appending index 0 to end of list
        rotor_2["rotor"].append(rotor_2["rotor"][0])
        rotor_2["rotor"].pop(0)
    return


def encrypt(starting_letter):
    """Encrypt input letters through same method as original Enigma (without plugboard)"""
    
    # Get the letter on each rotor at the alphabet's index of the previous letter
    rotor_3_letter = rotor_3["rotor"][alphabet.index(starting_letter)]
    # print(rotor_3_letter)
    rotor_2_letter = rotor_2["rotor"][alphabet.index(rotor_3_letter)]
    # print(rotor_2_letter)
    rotor_1_letter = rotor_1["rotor"][alphabet.index(rotor_2_letter)]
    # print(rotor_1_letter)
    reflector_letter = reflector_b[alphabet.index(rotor_1_letter)]
    # print(reflector_letter)
    rotor_1_reversed_letter = alphabet[rotor_1["rotor"].index(reflector_letter)]
    # print(rotor_1_reversed_letter)
    rotor_2_reversed_letter = alphabet[rotor_2["rotor"].index(rotor_1_reversed_letter)]
    # print(rotor_2_reversed_letter)
    final_letter = alphabet[rotor_3["rotor"].index(rotor_2_reversed_letter)]
    print(final_letter)



def main():
    global rotor_1
    global rotor_2
    global rotor_3

    # Initialise rotors to be used
    rotor_1 = all_rotors[0]
    rotor_2 = all_rotors[1]
    rotor_3 = all_rotors[2]
    

    rotate_rotors()
main()