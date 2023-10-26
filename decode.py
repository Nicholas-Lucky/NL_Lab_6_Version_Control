#Decode function implemented by Jayden Moore
#Takes an encoded password and decodes it with the inverse of the encode method
def decode(password):
    decoded_password = ""

    #Subtracts 3 from each integer within the password's string
    for i in password:
        decoded_password += str(int(i) - 3)
    return decoded_password