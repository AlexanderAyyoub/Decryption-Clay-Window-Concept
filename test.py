

def __init__(self,cipher_text,key,string):
        self.cipher_text = cipher_text
        self.key = key 
        self.string = string 
        
def generateKey(string, key):
        key = list(key)
        if len(string) == len(key):
            return key
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return ''.join(key)

def cipherText(string, key):
    cipher_text = []
    string = string.upper()
    key = key.upper()
    for i in range(len(string)):
        if string[i].isalpha():  # Check if the character is alphabetic
            x = (ord(string[i]) + ord(key[i % len(key)]) - 2 * ord('A')) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(string[i])  # Preserve spaces and non-alphabetic characters
    return ''.join(cipher_text)

def originalText(cipher_text, key):
    orig_text = []
    key = key.upper()
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():  # Check if the character is alphabetic
            x = (ord(cipher_text[i]) - ord(key[i % len(key)]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])  # Preserve spaces and non-alphabetic characters
    return ''.join(orig_text)

if __name__ == "__main__":
    keyword = input('Key: ')
    string = input("Message: ")
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))
