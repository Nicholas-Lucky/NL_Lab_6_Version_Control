# Nicholas Lucky's Lab 6
# Nicholas Lucky made this program's encode() function!
def print_menu():  # Prints the encoding/decoding menu to the user!
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(number):  # Takes a number, and adds 3 to each digit in the number!
    encoded_number = ""  # Stores the encoded number that will be returned back

    for digit in str(number):  # For each digit in the number...
        encoded_number += str(int(digit) + 3)  # Add 3 to the digit, and add the digit to encoded_number

    # Let the user know their password has been encoded and stored!
    print("Your password has been encoded and stored!\n")

    return encoded_number  # Return the encoded number back!

# TODO: Add the Decode function!

#Decode function implemented by Jayden Moore
#Takes an encoded password and decodes it with the inverse of the encode method
def decode(password):
    decoded_password = ""

    #Subtracts 3 from each integer within the password's string
    for i in password:
        decoded_password += str(int(i) - 3)
    return decoded_password

if __name__ == "__main__":
    
    """
    OPTIONAL: If you'd like to, since the user could immediately choose to decrypt a password at the start of the program,
              when no password as yet been inputted, you could put an if-statement later in the code to check
              if password != None, and proceed to decode the password/direct the user back appropriately!
    """
    password = None  # Stores the password the user is planning to encrypt
    encrypted_password = None  # Stores the encrypted password of the user's password
    decrypted_password = None # Stores the decrypted password of the user's password
    
    while True:  # Until the user chooses to exit the program...
    
        print_menu()  # Print the menu
    
        while True:  # Until the user inputs a valid menu option...
            try:  # Have the user input an option (in an integer from 1 to 3)
                user_option = int(input("\nPlease enter an option: "))
                if user_option not in [1, 2, 3]:  # If the user's number is not 1, 2, or 3...
                    raise Exception  # Raise an exception!
    
                break  # Otherwise, the user's option seems to be valid
    
            except ValueError:  # If the user does not input an integer...
                print("Your input seems to not be a number... try again!")  # ...let them know!
                continue  # Restart the try...except statement loop
    
            except Exception:  # If the user's option is not one of the menu options...
                print("Your input seems to be invalid... try again!")  # ...let them know!
                continue  # Restart the try...except statement loop
    
        if user_option == 1:  # If the user chooses to encode a password...
            while True:  # ...until the user inputs a valid password...
                try:  # Have the user input a password of integers
                    password = int(input("Please enter your password to encode: "))
                    for password_digit in str(password):  # Check each digit in the password
                        if int(password_digit) > 6:  # If a digit is greater than 6...
                            raise Exception  # Raise an exception!
    
                    break  # Otherwise, the user's password seems to be valid!
    
                except ValueError:  # If the user's password is not an integer...
                    print("Your input seems to not be a number... try again!")  # ...let them know!
                    continue  # Restart the try...except statement loop
    
                except Exception:
                    # ...let them know!
                    print("We will be shifting each digit up by 3, so make sure to keep every digit 6 or under!")
                    continue  # Restart the try...except statement loop
    
            encrypted_password = encode(password)  # Encode the user's password, and store it in encrypted_password
    
        # TODO: Implement the Decode function!
        elif user_option == 2:  # If the user chooses to decode a stored password...

            if encrypted_password is None:  # If the user hasn't stored a password yet...
                # Inform them off that!
                print("You don't seem to have a encoded password stored to decode, try encoding a password first!\n")
                continue  # Repeat the loop to allow the user to store a password

            decrypted_password = decode(encrypted_password)  # Otherwise, decrypt the stored password

            # Print out the encoded and decoded passwords to the user!
            print(f"The encoded password is {encrypted_password}, and the original password is {decrypted_password}.\n")
    
        elif user_option == 3:  # If the user chooses to exit the program...
            break  # Exit the program loop
