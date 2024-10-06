#18

def decrypt_text(input_file, output_file):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    decrypted_text = ''

    with open(input_file, 'r', encoding='utf-8') as infile:
        encrypted_text = infile.read()

        for char in encrypted_text:
            if char in alphabet:
                index = (alphabet.index(char) - 1) % len(alphabet)
                decrypted_text += alphabet[index]
            else:
                decrypted_text += char

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(decrypted_text)

decrypt_text('assets/encrypted.txt', 'decrypted.txt')
