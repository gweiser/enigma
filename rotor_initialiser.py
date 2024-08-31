import rotors # type: ignore

# Initialise lists for base rotor and alphabet
rotor_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Initialise 3 rotors and reflector
r1_rotor = rotors.rotor1
r2_rotor = rotors.rotor2
r3_rotor = rotors.rotor3
reflector = rotors.reflector


def initialiser(start_num):
    """Initialise a rotor and its counterpart"""
    rotor = []
    # Fill rotor with digits from start_num to 26
    for i in range(27-int(start_num)):
        rotor.append(i+start_num)
    # Fill up rest of rotor
    if len(rotor) < 26:
        for i in range(start_num-1):
            rotor.append(i+1)

    return rotor


def encrypt_number(r1, r2, r3, start_num):
    """Encrypt a letter using rotors and reflector"""
    # Get index of changed number in rotor1
    r1_new_index = r1.index(r1_rotor[start_num])
    # Get new number on rotor2 (at index of rotor1)
    r2_num = r2[r1_new_index]
    # Get index of changed number in rotor2
    r2_new_index = r2.index(r2_rotor[r2_num])
    # Get new number on rotor3
    r3_num = r3[r2_new_index]
    # Get index of changed number in rotor3
    r3_new_index = r3.index(r3_rotor[r3_num])
    # Get new number on reflector (at index of rotor3)
    reflector_num = rotor_base[r3_new_index]
    # Get index of changed number on reflector
    reflector_new_index = rotor_base.index(reflector[reflector_num])
    # Get new number on rotor3 (at index of reflector)
    r3_second_num = r3[reflector_new_index]
    # Get index of new number on rotor3
    r3_second_new_index = r3.index(r3_rotor[r3_second_num])
    # Get new number on rotor2 (At index of rotor3)
    r2_second_num = r2[r3_second_new_index]
    # Get index of changed number on rotor2
    r2_second_new_index = r2.index(r2_rotor[r2_second_num])
    # Get new number on rotor1 (at index of rotor2)
    r1_second_num = r1[r2_second_new_index]
    # Get index of encrypted number on rotor1
    r1_second_new_index = r1.index(r1_rotor[r1_second_num])
    # Encrypted number
    encrypted_num = r1[r1_second_new_index]

    return encrypted_num


def main():
    """Main script"""
    # Starting numbers for each rotor
    r1_startnum = 1
    r2_startnum = 13
    r3_startnum = 22
    # Initialise keypress and rotation counters
    keypresses = 0
    r1_rotations = 0
    r2_rotations = 0


    while True:
        # Initialise 3 rotors
        r1 = initialiser(r1_startnum+keypresses)
        r2 = initialiser(r2_startnum+r1_rotations)
        r3 = initialiser(r3_startnum+r2_rotations)
        # Get plaintext letter
        plaintext_letter = input("Input: ").upper()
        # Get letter's number
        plaintext_num = alphabet.index(plaintext_letter) + 1
        # Encrypt number 
        encyrpted_num = encrypt_number(r1, r2, r3, plaintext_num)
        # Get encrpyted letter
        encyrpted_letter = alphabet[encyrpted_num-1]

        # Rotate rotors depending on value of keypresses
        keypresses += 1
        if keypresses == 26:
            keypresses = 0
            r1_rotations += 1
        if r1_rotations == 26:
            r1_rotations = 0
            r2_rotations += 1
        if r2_rotations == 26:
            r2_rotations = 0

        print(encyrpted_letter)
        print(r1)
        print(r2)
        print(r3)



main()