
# This is the password encoder that will be used to make keys.
keyList = ["A","B","C","D","E","F","G","H","I","J",\
    "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]



def userCode():
    userInput = input("\n\n\n\n------------\
        -----------\nPlease provide a code to be ciphered.\nCode: ")
    return userInput


# The functions takes in a code or phrase by the user and converts it 
# to index postion as its position in the Keylists alphabets.
def codeToIndex(password):

    global indexForCode
    global code
    code = password
    indexForCode = []

    # The loop goes through each alphabet in the code/password the user wants to code.
    for alphabet in password:
        if (alphabet.upper() not in keyList) and (alphabet != " "):
                return -1


        # The if alphabet checks for spaces in the code/password provided by the user.
        if alphabet == " ":
                # If there is a spaces, it is appended to the index list for the code(indexForCode).
                indexForCode.append(" ")
                continue

        # The loop goes through the index position of the alphabets in the keylist.
        for alphabetIndex in range(0,len(keyList)):

            # if the alaphabet in the code/password matches the 
            # alphabet in the keylist, the index of the alphabet in the1 keylist 
            # is appended to the indexForCode list.
            if alphabet.upper() == keyList[alphabetIndex]:
                indexForCode.append(alphabetIndex)
# codeToIndex(userCode())

# This functon ask for the key number
def inputKey():
    # This control flow will ask for the key
    try:
        keyNumber = int(input("\nWhat is the key number from 1-25?\nKey:"))
        # If key is not between 1 and 25, it will produce an error
        if  1 > keyNumber or keyNumber >= 26:
            print("\nPlease provide Key from 1-25")
            return None
        else:
            return keyNumber
    except:
        print("\nPlease provide Key from 1-25")
        return None
        
            


# This function takes in the number of the key from the user 
# wants to use and creates the encoded index
def indexToEncodeIndex (key):
    
    # This is the list which will contain the encoded index
    global encodedIndex
    encodedIndex = []
    # If the inputKey returns None
    if key == None:
        return None

    # The loop goes through each index number for the code
    for index in indexForCode:
        # if there is a space, the space is appended to the encoded index list
        if index == " ":
            encodedIndex.append(index)
        
        # if the element is a index number, it goes through this:
        else:
            # they key number is added to the index, the new index will change alphabet that is outputted
            index+= key
            # if the index, after the key is applied, >= to 26, the if statment takes it back to the
            # begenning of the key list
            if index >= 26 :
                index= index - 26
            # if the index, after the key is applied, is not >= to 26, the index is appended
            encodedIndex.append(index)
    print(encodedIndex)



# This fucntion coverts the encoded index to encoded strings
def encodedIndexToCode():
    # This is the string to which every encoded letter or word will be appended to
    string = ""
    if encodedIndex == []:
        return None

    # The loop iterates through all the index in encodedIndex list
    for number in encodedIndex:

        # Checks for space
        if number != " ":
            # Checks for the capatlization of the letters
            # if the letter is lowercase, it appends the corresponding lowercase letter
            # /*The number is passed into enodedIndex.index to find the index of the number
            # /*The index of the number is passed into the code[], which outputs the alaphabet in the password
            # /*at the same location. Then it is checked it is checked for lowercase
            if code[encodedIndex.index(number)] == code[encodedIndex.index(number)].lower():
                string+= keyList[number].lower()
                encodedIndex[encodedIndex.index(number)] = -1
            # if the letter is uppercase, it appends the coresponding uppercase letter
            else:
                string+= keyList[number]
                encodedIndex[encodedIndex.index(number)] = -1
        # This checks for the space in the encodedIndex list
        else:
            string+= number
    print("\nEncoded Code: " + string)

# print(encodedIndexToCode())


# Main screen
def mainScreen():
    try:
        while True:
            # This asks for the user input (1 or 2) and returns
            userInput = int(input("\n\n\n\n---Security Cipher---\n1.) Encode\n2.) Quit\nChoose Navigation number: "))
            if userInput in (1,2):
                return userInput
            else:
                print("Invalid Input")
    except:
        print("Invalid input")

# mainScreen()

def error():
    print("\t--Error--\n--Please provide correct input--")

def control():
    input("Back to Main Menu")
    return


def main():
    while True:
        main = mainScreen()
        # Encode
        if main == 1:
            # Looping to return to main screen when code is encrypted
            while True:
                controlCheck = codeToIndex(userCode())
                if controlCheck == -1:
                    error()
                    control()
                    break
                else:
                    indexToEncodeIndex(inputKey())
                    encodedIndexToCode()
                    control()
                    break
        # Quit
        elif main == 2:
            print("\n\n\n\n\nThank you.")
            break
        
if __name__=="__main__":
    main()





    

                
            
    






