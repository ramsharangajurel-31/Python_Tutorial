def rail_fence_encrypt(plaintext, rails):
    rail_matrix = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for char in plaintext:
        if row == 0 or row == rails - 1:
            direction *= -1
        rail_matrix[row][col] = char
        col += 1
        row += direction

    ciphertext = []
    for r in rail_matrix:
        for char in r:
            if char != '\n':
                ciphertext.append(char)

    return ''.join(ciphertext)


def rail_fence_decrypt(ciphertext, rails):
    rail_matrix = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        if row == 0 or row == rails - 1:
            direction *= -1
        rail_matrix[row][col] = '*'
        col += 1
        row += direction

    index = 0
    for r in rail_matrix:
        for j in range(len(r)):
            if r[j] == '*' and index < len(ciphertext):
                r[j] = ciphertext[index]
                index += 1

    plaintext = []
    row, col = 0, 0
    direction = -1

    for _ in range(len(ciphertext)):
        if row == 0 or row == rails - 1:
            direction *= -1
        plaintext.append(rail_matrix[row][col])
        col += 1
        row += direction

    return ''.join(plaintext)


plaintext = input("Enter the plain text: ")
rails = int(input("Enter the no of rails/depth: "))

encrypted_text = rail_fence_encrypt(plaintext, rails)
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)