def initialiser(start_num):
    rotor = []
    # Fill rotor with digits from start_num to 26
    for i in range(27-int(start_num)):
        rotor.append(i+start_num)
    # Fill up rest of rotor
    if len(rotor) < 26:
        for i in range(start_num-1):
            rotor.append(i+1)

    return rotor
    
    


def main():
    rotor_num = int(input("Number of rotors: "))
    rotors = {}
    for rotor in range(rotor_num):
        start_num = int(input("Starting number: "))
        rotors[rotor] = initialiser(start_num)

    # start_num = int(input("Starting number: "))
    # rotor = initialiser(start_num)
    for i in rotors:
        print(rotors[i])


main()