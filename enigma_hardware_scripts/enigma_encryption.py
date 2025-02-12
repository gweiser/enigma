"""Enigma I emulation (no plugboard)"""
# Result variable for telling Rotor Config Interface (hardware) if rotor positon needs to be advanced on LCD
result = 0
# Alphabet reference
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Reflectors
reflector_b = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Rotor configurations
all_rotors = [
    {
        "rotor": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "turnover": "Q"
    },
    {
        "rotor": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "turnover": "E"
    },
    {
        "rotor": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "turnover": "V"
    },
    {
        "rotor": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "turnover": "J"
    },
    {
        "rotor": "VZBRGITYUPSDNHLXAWMJQOFECK",
        "turnover": "Z"
    }
]

def initialise_rotor_position(rotor, position):
    """Rotate rotor to the correct starting position"""
    shift = int(position) - 1  # Convert to zero-based index
    rotor["rotor"] = rotor["rotor"][shift:] + rotor["rotor"][:shift] 

def initialise_ring_setting(rotor, ring_setting):
    """Initialise rotor's ring setting"""
    # Shifts the rotor by the amount of offset required, same effect as offsetting the alphabet (relative difference is important)
    shift = int(ring_setting) - 1  # Convert to zero-based index
    # Offset rotor
    rotor["rotor"] = rotor["rotor"][shift:] + rotor["rotor"][:shift]
    # Change turnover letter by offsetting it the same amount as ring setting
    rotor["turnover"] = alphabet[(alphabet.index(rotor["turnover"]) - shift) % 26]  

def rotate_rotors(rotor_1, rotor_2, rotor_3):
    """Simulate rotor stepping mechanism"""
    # Step rotor 3 with every keypress
    rotor_3["rotor"] = rotor_3["rotor"][1:] + rotor_3["rotor"][:1]
    result = 0
    

    # If rotor 3 hits its turnover position, rotate rotor 2
    if rotor_3["rotor"][0] == rotor_3["turnover"]:
        rotor_2["rotor"] = rotor_2["rotor"][1:] + rotor_2["rotor"][:1]
        result = 1
        # If rotor 2 also hits its turnover position, rotate rotor 1
        if rotor_2["rotor"][0] == rotor_2["turnover"]:
            rotor_1["rotor"] = rotor_1["rotor"][1:] + rotor_1["rotor"][:1]
            result = 2


def encrypt(letter, rotor_1, rotor_2, rotor_3):
    """Encrypt a single letter"""
    index = alphabet.index(letter)  # Convert letter to index

    # Forward through rotors
    letter = rotor_3["rotor"][index]
    letter = rotor_2["rotor"][alphabet.index(letter)]
    letter = rotor_1["rotor"][alphabet.index(letter)]

    # Reflector
    letter = reflector_b[alphabet.index(letter)]

    # Backward through rotors
    letter = alphabet[rotor_1["rotor"].index(letter)]
    letter = alphabet[rotor_2["rotor"].index(letter)]
    letter = alphabet[rotor_3["rotor"].index(letter)]

    # Rotate rotors after each key press
    rotate_rotors(rotor_1, rotor_2, rotor_3)

    return letter




# Main function
# def main():
#     global rotor_1, rotor_2, rotor_3

#     # Choose rotors to use
#     rotor_1 = all_rotors[0]
#     rotor_2 = all_rotors[1]
#     rotor_3 = all_rotors[2]

#     # Get starter positions
#     rotor_1_starter = int(input("Rotor 1 starter position: "))
#     rotor_2_starter = int(input("Rotor 2 starter position: "))
#     rotor_3_starter = int(input("Rotor 3 starter position: "))

#     # Get ring settings
#     rotor_1_ring = int(input("Rotor 1 ring setting: "))
#     rotor_2_ring = int(input("Rotor 2 ring setting: "))
#     rotor_3_ring = int(input("Rotor 3 ring setting: "))

#     # Set rotors to correct positions
#     initialise_rotor_position(rotor_1, rotor_1_starter)
#     initialise_rotor_position(rotor_2, rotor_2_starter)
#     initialise_rotor_position(rotor_3, rotor_3_starter)


#     # Set ring settings
#     initialise_ring_setting(rotor_1, rotor_1_ring)
#     initialise_ring_setting(rotor_2, rotor_2_ring)
#     initialise_ring_setting(rotor_3, rotor_3_ring)

#     # Main encryption loop
#     while True:
#         # Get letter to encrypt
#         letter = input("Letter to encrypt: ").upper()
#         # Encrypt letter
#         encrypted_letter = encrypt(letter)
#         print(f"Encrypted letter: {encrypted_letter}")

# main()
