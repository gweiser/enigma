rotor_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# Counterparts for each of the five rotors (originals were also hard-coded)
counterparts = {
    1: [2, 16, 26, 21, 12, 5, 13, 18, 17, 25, 20, 23, 10, 1, 7, 4, 22, 11, 24, 19, 8, 14, 6, 9, 3, 15],
    2: [1, 6, 7, 26, 25, 2, 23, 12, 15, 8, 4, 17, 11, 14, 24, 20, 13, 9, 10, 16, 3, 22, 21, 5, 19, 18],
    3: [20, 21, 7, 26, 24, 13, 6, 11, 5, 25, 15, 22, 3, 4, 16, 14, 17, 12, 10, 1, 19, 9, 8, 23, 18, 2],
    4: [25, 7, 26, 17, 1, 8, 3, 6, 22, 24, 19, 4, 20, 2, 11, 23, 10, 16, 15, 18, 9, 14, 13, 5, 12, 21],
    5: [17, 11, 8, 14, 23, 24, 12, 3, 10, 6, 5, 2, 19, 13, 25, 21, 20, 1, 9, 16, 4, 15, 18, 7, 26, 22]
}


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

    # print(r1["rotor"])
    # print(r1["counterpart"])
    # print(r2["rotor"])
    # print(r2["counterpart"])
    # print(r3["rotor"])
    # print(r3["counterpart"])

    index = r1["rotor"].index(start_num)
    r1_counterpart = r1["counterpart"][index]
    r2_counterpart = r2["counterpart"][index]
    r3_counterpart = r3["counterpart"][index]




    



main()