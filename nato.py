
# I found A was spelled both "alpha" and "alfa", apparently alfa is the correct way for nato
def main():
    nato_alphabet = {
        'a': 'Alfa',
        'b': 'Bravo',
        'c': 'Charlie', 
        'd': 'Delta', 
        'e': 'Echo',
        'f': 'Foxtrot', 
        'g': 'Golf', 
        'g': 'Hotel', 
        'i': 'India', 
        'j': 'Juliet',
        'k': 'Kilo', 
        'l': 'Lima', 
        'm': 'Mike', 
        'n': 'November', 
        'o': 'Oscar',
        'p': 'Papa', 
        'q': 'Quebec', 
        'r': 'Romeo', 
        's': 'Sierra', 
        't': 'Tango',
        'u': 'Uniform', 
        'v': 'Victor', 
        'w': 'Whiskey', 
        'x': 'X-ray', 
        'y': 'Yankee',
        'z': 'Zulu'


    }
    # It only works in lower case, i dont know how to make it work with uppercase also
    translate = input("Enter an word to translate (In lower case): ")
    print("NATO Phonetic Alphabet:")
    for letter in translate:
            print(nato_alphabet[letter])
main()