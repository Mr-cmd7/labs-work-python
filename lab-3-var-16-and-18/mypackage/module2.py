def decrypt_text(filename, output_filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    decrypted_text = ''
    for char in text:
        if 'а' <= char <= 'я':
            decrypted_text += chr(ord(char) - 1) if char != 'а' else 'я'
        elif char == 'ё':
            decrypted_text += 'е'
        else:
            decrypted_text += char

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(decrypted_text)


if __name__ == "__main__":
    decrypt_text('resources/encrypted.txt', 'resources/decrypted.txt')
