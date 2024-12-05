from mypackage.module1 import find_min_year
from mypackage.module2 import decrypt_text

if __name__ == "__main__":
    min_year = find_min_year('mypackage/resources/dates.txt')
    print(f"Год с наименьшим номером: {min_year}")

if __name__ == "__main__":
    decrypt_text('mypackage/resources/encrypted.txt', 'mypackage/resources/decrypted.txt')