letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z']



def cypher_text():
    task=input("for 'ENCODE' press 'E' and for 'DECODE' press 'D'...\n").lower()
    shift=int(input("Ente Shift Number.\n"))
    shift=shift % 26

    str1=""
    for letter in msg:
        possition= letters.index(letter)
        if task=="e":
            new_possition = possition+shift
        elif task=="d":
            new_possition = possition-shift
        else:
            print("Please type only E or D.")
            break       
        new_letter = letters[new_possition]
        str1+=new_letter
    
    if task=="e":
        print(f"The Encoded string is : {str1}")
    elif task=="d":
        print(f"The Decoded string is : {str1}")
cypher_text()