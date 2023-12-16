import random

default_data = 'some string'

alphabet = 'qwertyuiopasdfghjklzxcvbnm' + 'qwertyuiopasdfghjklzxcvbnm'.upper()
alphabet_len = len(alphabet)


def data_to_bin(data):
    return ''.join(format(ord(_), '08b') for _ in data)


def data_to_char(data):
    result = ''
    for c in [data[i:i + 8] for i in range(len(data)) if not i % 8]:
        result += chr(int(c, 2))
    return result


def encrypt(data):
    data_len = len(data)
    data_bin = data_to_bin(data)
    key = ''
    for i in range(data_len):
        k = alphabet[random.randint(0, alphabet_len - 1)]
        key += k
    key_bin = data_to_bin(key)
    result = ''

    for i, c in enumerate(data_bin):
        result += str(int(c) ^ int(key_bin[i]))
    return result, key


def decrypt(data, key):
    decoded_data = ''
    key_bin = data_to_bin(key)
    for i, c in enumerate(data):
        decoded_data += str(int(c) ^ int(key_bin[i]))

    return decoded_data, data_to_char(decoded_data)


if __name__ == '__main__':
    print("Нажимайте Enter для подставления дефолтных значений")
    input_data = input("Введите текст: ")
    if input_data == '':
        input_data = default_data
    encrypt_data_bin, key = encrypt(input_data)
    print("Зашифрованный текст: \n" + encrypt_data_bin)
    print("Ключ: \n" + key)
    decrypt_data_bin, decrypt_data = decrypt(encrypt_data_bin, key)
    print("Расшифрованный текст: \n" + decrypt_data)