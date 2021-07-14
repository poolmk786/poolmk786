"""ITECH1400 - FOUNDATIONS OF PROGRAMMING.
Assignment 01: Ceaser Ciphers and Turtle Graphics
Sanakkayala Venkatesh
Student ID: 30382829"""


# Creating modes of operation for the Ceaser Cipher Application using "if" statement
def ModeSelect():
    print("------------>>> Caesar Cipher Algorithm  <<<------------")
    mode_selector = int(input("Please select mode of operation for the Cipher Algorithm. "
                              "\n 1.Encryption Mode "
                              "\n 2.Decryption Mode "
                              "\n  Input '1' for Encryption mode OR '2' for Decryption mode --> "))
#If user selects, "1", the application enters Encryption Mode
    if mode_selector == 1:
        #Message to User that he/she has selected Encryption mode
        print("------>  Entering Encryption Mode!  <------")
        #Asks for an input file
        filename = str(input("Enter the Full file name for plain text file: "))
        #Asks the user for a Key value in integer
        key = int(input("Enter the Key that you want to encrypt the data with: "))
        #Message showing that the parameters entered are being processed.
        print("Encrypting file,", filename, " with the Key,", key, "& saving it to cipher.txt")
        # Algorithm for Encryption
        #Function of Encryption to call later
        def encrypt(PlainText, Key):
            #initialising values
            outText = []
            cryptText = []
            #Creatina a list of Characters in Uppercase to compare with the characters in text file
            uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            # Creatina a list of Characters in Lowercase to compare with the characters in text file
            lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
            # Creatina a list of Characters in symbols, spaces and new lines to compare with the characters in text file
            spaces = [' ', '\n', '!', '"','#','$','%','&','(',')','.',',',':',';','[',']','{','}','^','&','*', '=', '+','-','_','/']
            # Creatina a list of Characters in Integers to compare with the characters in text file
            numbers = ['0', '1', '2','3','4','5','6','7','8','9']
            #Function to Convert List items to string
            def listToString(s):

                # initialize an empty string
                str1 = ""

                # traverse in the string
                for ele in s:
                    str1 += ele
                # return string
                return str1
            #Loop to compare every character in the File
            for eachLetter in PlainText:
                #Compares and changes value from Uppercase according to the key
                if eachLetter in uppercase:
                    index = uppercase.index(eachLetter)
                    #Applying modulus to get the remainder as the index of new letter (if eachletter is "Z", the new letter then remainder index
                    crypting = (index + Key) % 26
                    cryptText.append(crypting)
                    newLetter = uppercase[crypting]
                    #Adding to the list as a character
                    outText.append(newLetter)
                #Same process for lowercase letters
                elif eachLetter in lowercase:
                    index = lowercase.index(eachLetter)
                    crypting = (index + Key) % 26
                    cryptText.append(crypting)
                    newLetter = lowercase[crypting]
                    outText.append(newLetter)
                #Same process for symbols, spaces and newlines
                elif eachLetter in spaces:
                    index = spaces.index(eachLetter)
                    newLetter = spaces[index]
                    outText.append(newLetter)
                #Same process for numbers
                elif eachLetter in numbers:
                    index = numbers.index(eachLetter)
                    #Applying modulus of 10 because the total number of digits is 10
                    crypting = (index + Key) % 10
                    cryptText.append(crypting)
                    newLetter = numbers[crypting]
                    outText.append(newLetter)
            #Creating a new name for the cipher file with same extension
            cipher_name = "cipher-"+filename
            print("The file hase been encrypted and has been saved to, " + cipher_name)
            #opens the new file with WRITE mode
            cipher_file = open(cipher_name, "w+")
            #Creates the lists to strings and adds to the file
            cipher_file.write(listToString(outText))
            #Not all users want to get their cipher text displayed after encrypting. Hence, asking the user if they want to view the text in console.
            select_view = str(
                input("Enter 'y' if you want to view the Encrypted text now. \n OR 'n' if you do not want to."))
            if select_view == "y":
                print(listToString(outText))
            elif select_view == "n":
                print("The Encrypted text(Cipher) has been saved.")
            else:
                print("The command entered is invalid, Thanks for using the Application. Bye !")
            return outText


        # Opens the file in READ mode & calls the enrypt function
        plain_text_file = open(filename, "r")
        if plain_text_file.mode == 'r':
            plain_text_content = plain_text_file.read()
            print("----> Encrypting <---")
            encrypt(plain_text_content, key)

    #If user selects 2, the application works in Decryption Mode
    elif mode_selector == 2:
        print("------>  Entering Decryption Mode!  <------")
        #asks for the file to decrypt
        filename = str(input("Enter the Full file name for the Encrypted file: "))
        #Asks for a key
        key = int(input("Enter the Key to decrypt the cipher: "))
        print("Decrypting file,", filename, " with the Key,", key, "& saving it with Plain text in a file.")
        # Algorithm for Decryption goes here
        #Decryption function to call later & is implemented similar to Encryption function
        def decrypt(CryptText, Key):
            outText = []
            EncryptText = []

            uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
            spaces = [' ', '\n', '!', '"','#','$','%','&','(',')','.',',',':',';','[',']','{','}','^','&','*', '=', '+','-','_','/']

            numbers = ['0', '1', '2','3','4','5','6','7','8','9']

            #Function to Convert List items to string
            def listToString(s):

                # initialize an empty string
                str1 = ""

                # traverse in the string
                for ele in s:
                    str1 += ele
                # return string
                return str1
            #loops for each letter in the file
            for eachLetter in CryptText:
                if eachLetter in uppercase:
                    index = uppercase.index(eachLetter)
                    crypting = (index - Key) % 26
                    EncryptText.append(crypting)
                    newLetter = uppercase[crypting]
                    outText.append(newLetter)
                elif eachLetter in lowercase:
                    index = lowercase.index(eachLetter)
                    crypting = (index - Key) % 26
                    EncryptText.append(crypting)
                    newLetter = lowercase[crypting]
                    outText.append(newLetter)
                elif eachLetter in spaces:
                    index = spaces.index(eachLetter)
                    newLetter = spaces[index]
                    outText.append(newLetter)
                elif eachLetter in numbers:
                    index = numbers.index(eachLetter)
                    crypting = (index - Key) % 10
                    EncryptText.append(crypting)
                    newLetter = numbers[crypting]
                    outText.append(newLetter)
            OriginalFile_name = "Decrypted-"+filename
            print("The file hase been decrypted and has been saved to," + OriginalFile_name)
            cipher_file = open(OriginalFile_name, "w+")
            cipher_file.write(listToString(outText))
            select_view = str(input("Enter 'y' if you want to view the Decrypted file now. \n OR 'n' if you do not want to."))
            if select_view == "y":
                print(listToString(outText))
            elif select_view =="n":
                print("The decrypted text(Original message) has been saved." )
            else:
                print("The command entered is invalid, Thanks for using the Application. Bye !")
            return outText


        # Opens the files and performs decrypt mode
        crypt_text_file = open(filename, "r")
        if crypt_text_file.mode == 'r':
            crypt_text_content = crypt_text_file.read()
            print("----> Decrypting <---")
            decrypt(crypt_text_content, key)
    #If user selects other than 1 or 2 in Step 1, the application says that the selection is invalid.
    else:
        print("Invalid Input to select Modes of operation.")
        print("Please input either of the following options shown to select a mode.")
        reselect = str(input("Do you want to try again ? \n Input 'y' to go back to selecting modes."))
        if reselect == "y":
            ModeSelect()
        else:
            print("You have selected to quit the application. \n Thank you for using Ceaser Cipher Application.")

#Calls the function to select modes and starts the application
ModeSelect()
