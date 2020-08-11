# ///This program will decode the password using the provided key

# This is the key list. it will be used to dencode the passcode
keyList = ["A","B","C","D","E","F","G","H","I","J",\
    "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# This function will ask the the user to input the password
def inputPassword():
    password = input("\n\n\n\n------------\
        -----------\nPlease provide a code to be decoded.\nCode: ")
    for i in password:
        if i.upper() not in (keyList or " "):
            print("\n\t--Error--\n--Please enter alphabet only--")
            return -1
        else:
            return password

# This function will ask for the user to input the key
def inputKey():
    # To check if the key is between 1-26
    key = input("\nWhat is the key number from 1-26? \nKey: ")
    if key.lower() == 'back':
        return -2
    elif int(key) not in range(0,27):
        print("\n\t---Error---\n--Please enter the correct key or type 'back' to go back--")
        return -1
    else:
        return int(key)

# This function takes in the password from inputPassword() and converts it into index
def passwordToIndex(inputPassword):
    # the parameter is set equal to the variable password
    password = inputPassword
    # This is the list to which the index of each alphabet in the password will be appended to
    encodedIndex = []

    # The for loop iterates through each unique alphabet in the password
    for alphabet in password:
        # this if statment checks if the alphabet is a space
        if alphabet != " ":
            # The for loop iterates through each alaphabet index in the key list
            for keyListAlphabet in range(0,len(keyList)):
                # this if statment will check if the alphabet is equal to the alphabet in the key list
                # if yes, the index of the alphabet in the key list is appended to the indexList
                # else, it continues to iterate through each alphabet in password, and thorugh the 
                # index of each alphabet in the key list
                if alphabet.upper() == keyList[keyListAlphabet]:
                    encodedIndex.append(keyListAlphabet)
        # if the alphabet is space, it is appended to the indexList as space
        elif alphabet == " ":
            encodedIndex.append(" ")
        # if the password is set to nothing, the function will return nothing
        else: 
            return None
    return encodedIndex

# This function will decode the encoded index from the passwordToIndex()
# it takes in the encoded index and the key provided in inputKey() function
def decodeIndex(encodedIndex, key):
    # This is the list to which the decoded index will be appended to
    decodedIndex = []

    # The loop goes through each index in the function encodedIndex()
    for index in encodedIndex:
        # /*if the index equals space
        if index !=" ":
        # /*if the index-key is less than 0:
            if (index-key) < 0:
                # the index is set equal to 26 added to the negative number produced by
                # index-key. The index is then is appended to decodedIndex
                index = 26+(index-key)
                decodedIndex.append(index)
            # /*if the (index - key) is greater than 0, 
            elif (index-key) >= 0:
                # index is set to (index-key), and is appended to decodedIndex
                index-=key
                decodedIndex.append(index)
            # /*if the index is equal to space, it is appended
        elif index == " ":
            decodedIndex.append(" ")
        else:
            return None
    return decodedIndex

# This function takes in the decodedIndex and returns the decoded password as a string
def indexToString(decodeIndex):
    # the string to which the decoded alphabets will be appended to
    string = ""
    # the for loop iterates through index in the decodeIndex
    for index in decodeIndex:
        # /*if the index does not equal space:
        if index != " ":
            # the index is passed into keylist, which outputs the decoded alphabet
            # then it is added to the string
            alphabet = keyList[index]
            string+=alphabet
        # /*if the index does equal space
        elif index == " ":
            # the space is added to the string
            string+= index
    return string

# this fuction checks if the alphabet is meant to be lower case or uppercase
def checkCase(decodedPassword, encodedPassword):
    # The string to which the correctly cased decoded password will be appended to
    string=""
    # the for loop goes through alpahbet index in the decodedPassword variable
    for index in range(0,len(decodedPassword)):
        # if the alphabet at index in encodedPassword is equal to the its lowercase alpahbet
        if encodedPassword[index]==encodedPassword[index].lower():
            # the alphabet at index in decodedPassword is converted to lowercase and
            # appended to the string
            string+=decodedPassword[index].lower()
        # if the alphabet at index in encodedPassword is not equlal to its lowercase
        # alphabet, or the the alphabet at index is actually a space. The alphabet is not
        # changed and appended to the string
        else:
            string+=decodedPassword[index]
    return string

# Main screen
def mainScreen():
    try:
        while True:
            # This asks for the user input (1 or 2) and returns
            userInput = int(input("\n\n\n\n---Security Cipher---\n1.) Decode\n2.) Quit\nChoose Navigation number: "))
            if userInput in (1,2):
                return userInput
            else:
                print("Invalid Input")
    except:
        print("Invalid input")

def control():
    input("Back to Main Menu")
    return

# Main Method
def main():
    while True:
        userInput = mainScreen()
        if userInput == 1:
            controlCheck1 = inputPassword()
            if controlCheck1 == -1:
                control()
                continue
            while True:
                controlCheck2 = inputKey()
                if controlCheck2 == -1:
                    continue
                elif controlCheck2 == -2:
                    break
                else:
                    enIndex = passwordToIndex(controlCheck1)
                    deIndex = decodeIndex(enIndex, controlCheck2)
                    string = indexToString(deIndex)
                    final = checkCase(string, controlCheck1)
                    print("\nDecoded test: {}".format(final))
                    control()
                    break


        if userInput == 2:
            print("\n\n\n\n\nThank you.")
            break


if __name__ == "__main__":
    main()












            




