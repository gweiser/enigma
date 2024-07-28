import rotors

rotor_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

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


def encrypt_number(r1, r1_rotor, r2, r2_rotor, r3, r3_rotor, start_num):
    """Encrypt a letter using rotors and reflector"""
    r1_new_index = r1.index(rotors.rotor1[start_num])
    r2_num = r2[r1_new_index]
    r2_new_index = r2.index(rotors.rotor2[r2_num])
    r3_num = r3[r2_new_index]
    r3_new_index = r3.index(rotors.rotor3[r3_num])
    r2_second_num = r2[r3_new_index]
    r2_second_new_index = r2.index(rotors.rotor2[r2_second_num])
    r1_second_num = r1[r2_second_new_index]
    r1_second_new_index = r1.index(rotors.rotor1[r1_second_num])

    encrypted_num = r1[r1_second_new_index]

    return encrypted_num

def main():
    # Starting number (letter A)
    start_num = 1
    r1 = initialiser(1)
    r2 = initialiser(13)
    r3 = initialiser(22)
    encyrpted = encrypt_number(r1, rotors.rotor1, r2, rotors.rotor2, r3, rotors.rotor3, start_num)

    # print(encyrpted)
    print(r1)
    print(r2)
    print(r3)



main()