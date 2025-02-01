"""Rotors"""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
reflector = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']
reflector_b = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

all_rotors = [
    ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'], # Turnover: Q
    ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'], # Turnover: E
    ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'], # Turnover: V
    ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'], # Turnover: J
    ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']  # Turnover: Z
]

def rotor_selection():
    """Choose three rotors"""
    rotors = []
    for i in range(0, 3):
        rotor_i = input(f"Rotor {i+1}: ")
        rotors.append(rotor_i)


    return rotors



def initialise_rotor_position():
    # TODO
    """Bring rotor into the desired starting position"""
    ...
    # Start list with letter corresponding to starter position (01 = A) and fill up rest oflist with remaining characters, wrap at Z


def initialise_rotor_ring():
    # TODO
    """Bring rotor ring position into desired state"""
    ...
    # ?


def rotate_rotor():
    # TODO
    """Rotate the rotors (change order of letters in list)"""
    ...
    # Rotate rotor 3 --> if rotor 3 is at its turnover position --> rotate rotor 2 --> if rotor 2 is at its turnover position --> rotate rotor 1




def encrypt(rotors_selected, starting_letter):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    rotor_1 = all_rotors[rotors_selected[0]-1]
    rotor_2 = all_rotors[rotors_selected[1]-1]
    rotor_3 = all_rotors[rotors_selected[2]-1]

    # Get the letter on each rotor at the alphabet's index of the previous letter
    rotor_3_letter = rotor_3[alphabet.index(starting_letter)]
    # print(rotor_3_letter)
    rotor_2_letter = rotor_2[alphabet.index(rotor_3_letter)]
    # print(rotor_2_letter)
    rotor_1_letter = rotor_1[alphabet.index(rotor_2_letter)]
    # print(rotor_1_letter)
    reflector_letter = reflector_b[alphabet.index(rotor_1_letter)]
    # print(reflector_letter)
    rotor_1_reversed_letter = alphabet[rotor_1.index(reflector_letter)]
    # print(rotor_1_reversed_letter)
    rotor_2_reversed_letter = alphabet[rotor_2.index(rotor_1_reversed_letter)]
    # print(rotor_2_reversed_letter)
    final_letter = alphabet[rotor_3.index(rotor_2_reversed_letter)]
    print(final_letter)

    




encrypt([1, 2, 3], input("Starting letter: ").upper())