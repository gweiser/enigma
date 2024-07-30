import rotors # type: ignore

rotor_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

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
    
    
def change_number(rotor_num, num):
    """Change a number inside a rotor"""
    changed_number = rotors.rotor_num[num]
    return changed_number


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
    # Starting number (letter A)
    start_num = 1
    r1 = initialiser(1)
    r2 = initialiser(13)
    r3 = initialiser(22)
    encyrpted = encrypt_number(r1, r2, r3, start_num)

    print(encyrpted)
    # print(r1)
    # print(r2)
    # print(r3)



main()