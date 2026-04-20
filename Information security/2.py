# Create a 5x5 matrix using a secret key
def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range(5)] for j in range(5)]
    letters_added = []

    # add the key to the matrix
    for letter in key:
        if letter not in letters_added and letter != 'J':
            letters_added.append(letter)

    # Add the rest of the alphabet (A-Z except J)
    for letter in range(65, 91):
        if letter == 74:  # skip J
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))

    # Fill matrix
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1

    return matrix


# Add fillers if same letter appears in a pair
def separate_same_letters(message):
    index = 0
    while index < len(message):
        l1 = message[index]
        if index == len(message) - 1:
            message += 'X'
            break
        l2 = message[index + 1]
        if l1 == l2:
            message = message[:index + 1] + "X" + message[index + 1:]
        index += 2
    return message


# Return index of a letter in matrix
def indexOf(letter, matrix):
    for i in range(5):
        if letter in matrix[i]:
            return (i, matrix[i].index(letter))
    return None


# Playfair cipher implementation
def playfair(key, message, encrypt=True):
    inc = 1 if encrypt else -1
    matrix = create_matrix(key)
    message = message.upper().replace('J', 'I').replace(' ', '')
    message = separate_same_letters(message)

    cipher_text = ""

    for l1, l2 in zip(message[0::2], message[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)

        if row1 == row2:  # same row
            cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        elif col1 == col2:  # same column
            cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        else:  # rectangle rule
            cipher_text += matrix[row1][col2] + matrix[row2][col1]

    return cipher_text


if __name__ == "__main__":
    plaintext = input("Enter message: ")
    secret_key = input("Enter secret key: ")

    cipherText = playfair(secret_key, plaintext)
    print("Encrypted:", cipherText)

    decrypted = playfair(secret_key, cipherText, False)
    print("Decrypted:", decrypted)