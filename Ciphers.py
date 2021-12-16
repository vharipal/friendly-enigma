#Test 1
def ceasar(text,shift):
    
    result = ""
    
    for i in range(len(text)):
        char = text[i]
    
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
    
        elif (char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char
            
    return result

text = "FDHVHU FLSKHU GHPR"
shift = -3
    
print ("Plain Text : " + text)
print ("Shift pattern : " + str(shift))
print ("Cipher: " + ceasar(text,shift))
print ("---------------", end= '\r')


#Test 2
#Loops through all possible values of shift to find the original text

def bruteForce(text,shift):
    
    result = ""
    
    for i in range(len(text)):
        char = text[i]
    
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
    
        elif (char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char
            
    return result

text = "FDHVHU FLSKHU GHPR"

for s in range (26):
    shift1 = -(s)
    print ("Plain Text : " + text)
    print ("Shift pattern : " + str(shift1))
    print ("Cipher: " + bruteForce(text,shift1), end= '\r')

print ("---------------", end= '\r')

#Test 4a
# transposition cipher
#rearranges 4 indexes of text at a time
#loops until end of text is reached

text = "PIRATEATTACK"

print ("Plain Text : " + text)

cipher = ""

mapping = [1, 3, 0 ,2]

for i in range (len(text)//len(mapping)):
    
    cipher += text[mapping[0]] + text[mapping[1]] + text[mapping[2]] + text[mapping[3]]
    
    text = text [len(mapping):]
    
print ("Cipher :", cipher, end= '\r')
print ("---------------", end= '\r')

#Test 4b
#Decrypts transposition cipher

text = "SWUETRAEOEHS"

print ("Unencrypted Cipher : " + text)

cipher = ""

mapping = [2, 0, 3, 1]

for i in range (len(text)//len(mapping)):
    
    cipher += text[mapping[0]] + text[mapping[1]] + text[mapping[2]] + text[mapping[3]]
    
    text = text [len(mapping):]

print ("Decrypted Cipher :", cipher)

