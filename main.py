

def shift_char(ch, sh):
    shifted = ord(ch) + sh

    if shifted > 90:
        return chr(65 + sh - (90 - ord(ch)))
    if shifted < 65:
        return chr(90 - (-sh - ord(ch) - 65))
    else:
        return chr(shifted)


def substitute(ch, k):
    char_index = k.index(ch)
    new_char = chr(char_index + 65)

    return new_char


def get_key():
    key = []
    for i in range(0, 26):
        key_char = input(chr(i + 65) + " is: ")
        while key.count(key_char) != 0 or key_char.__len__() > 1:
            key_char = input(chr(i + 65) + " is: ")
        key.append(key_char)

    return key


def main():
    cipher = input("Input '1' for Caesar Cipher, '2' for Mono-alphabetic Shift:")

    if cipher == 2:
        key = get_key()

    else:
        key = input("Shift by:")

    with open("file.txt") as f:
        for line in f:
            for ch in line:
                if ch != ' ' and ch != '\n':
                    if cipher == 2:
                        ch = substitute(ch, key)
                    else:
                        ch = shift_char(ch, int(key))
                print(ch, end=" ")


if __name__ == '__main__':
    main()
