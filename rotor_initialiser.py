rotor_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

def initialiser(rotor_num, start_num):
    """Initialise a rotor and its counterpart"""
    rotor = []
    # Fill rotor with digits from start_num to 26
    for i in range(27-int(start_num)):
        rotor.append(i+start_num)
    # Fill up rest of rotor
    if len(rotor) < 26:
        for i in range(start_num-1):
            rotor.append(i+1)

    # Counterpart to rotor (changing of value)
    counterpart = []
    for num in rotor:
        # Append corresponding counterpart to number
        counterpart.append(counterparts[rotor_num][rotor_base.index(num)])

    initialised = {
        "rotor": rotor,
        "counterpart": counterpart
    }
    return initialised
    
    
def change_number(rotor_num, num):
    """Change a number through a rotor"""
    rotor_index = rotor_base.index(num)
    counterpart_num = counterparts[rotor_num][rotor_index]
    return counterpart_num



def main():
    # Starting number (letter A)
    start_num = 1
    # Initialise rotors
    r1_rotor = 1
    r1_start = 5
    r2_rotor = 2
    r2_start = 7
    r3_rotor = 3
    r3_start = 9

    r1 = initialiser(r1_rotor, r1_start)
    r2 = initialiser(r2_rotor, r2_start)
    r3 = initialiser(r3_rotor, r3_start)





    



main()