encrypted_letters = {
    "a": "/",
    "b": "%",
    "c": "+",
    "d": "(",
    "e": "!",
    "f": "#",
    "g": "^",
    "h": "$",
    "i": ")",
    "j": "|",
    "k": "~",
    "l": "`",
    "m": "<",
    "n": ">",
    "o": ".",
    "p": "?",
    "q": ":",
    "r": "-",
    "s": "=",
    "t": "'",
    "u": "]",
    "v": "[",
    "w": "0",
    "x": "_",
    "y": ";",
    "z": ","
}

decrypted_letters = {
    "/": "a",
    "%": "b",
    "+": "c",
    "(": "d",
    "!": "e",
    "#": "f",
    "^": "g",
    "$": "h",
    ")": "i",
    "|": "j",
    "~": "k",
    "`": "l",
    "<": "m",
    ">": "n",
    ".": "o",
    "?": "p",
    ":": "q",
    "-": "r",
    "=": "s",
    "'": "t",
    "]": "u",
    "[": "v",
    "0": "w",
    "_": "x",
    ";": "y",
    ",": "z"
}

def encrypt(input_from_user):
    output_str = ""

    for letter in input_from_user.lower():
        output_str += encrypted_letters.get(letter, letter)
    
    print(output_str)


def decrypt(input_from_user):
    output_str = ""

    for letter in input_from_user.lower():
        output_str += decrypted_letters.get(letter, letter)

    print(output_str)

print("Shift ctrl c for copying, Shift ctrl d for pasting.")
option = input("Encrypt (e) or decrypt (d)?: ")

if option.lower() == "e":
    encrypt(input("Insert your message you want to encrypt: "))
elif option.lower() == "d":
    decrypt(input("Insert your message you want to decrypt: "))