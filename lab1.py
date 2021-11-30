class Caesar():
    text: str = None
    pattern: int = None

    def __init__(self, text: str = "", pattern: int = 0):
        self.text = text
        self.pattern = pattern

    def encrypt(self):
        if not self.text:
            raise ValueError('No text provided to cipher!')
        result = ''
        for i, char in enumerate(self.text):
            if char.isupper():
                result += chr((ord(char) + self.pattern - 65) % 26 + 65)

            else:
                result += chr((ord(char) + self.pattern - 97) % 26 + 97)

        return result

    def decrypt(self, message):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        for char in message:
            if char in LETTERS:
                idx = LETTERS.find(char) - self.pattern
                if idx < 0:
                    idx += len(LETTERS)

                result += LETTERS[idx]
            else:
                result += char
        return result


if __name__ == '__main__':
    flag=1
    print('Ceaser Encryption\n')

    while flag:
        a = Caesar()
        a.text = input('Input text: ')
        a.pattern = int(input('Enter key: '))

        print('------------------------------')
        print(f'Encrypted text: {a.encrypt()}')
        print(f'Decrypted text: {a.decrypt(a.encrypt())}')
