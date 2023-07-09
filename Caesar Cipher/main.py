import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2

def code():
    global alphabet
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 26
    def cypher(text,shift,direction) :
        new_text=""
        if direction=="decode" :
            shift *= -1            
        for char in text :
            if char in alphabet:
                position=alphabet.index(char)
                new_text += alphabet[position+shift]                
            else:
                new_text+= char
                
        print(f"The {direction}d text is {new_text}")    
    cypher(text,shift,direction)   
    choice=input("Do you want to run the code again(y/n) :")
    if choice in "Yy":
        code()
code()        