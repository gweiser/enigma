def initialiser(start_num):
    rotor = []
    for i in range(27-int(start_num)):
        rotor.append(i+start_num)
    if len(rotor) < 26:
        for i in range(start_num-1):
            rotor.append(i+1)

    return rotor
    
    


def main():
    start_num = int(input("Starting number: "))
    rotor = initialiser(start_num)
    print(rotor)


main()