"""
File: caesar.py
Name: leo HUNG
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program can decipher the cipher we input and create based on ALPHABET table.
    We can first create a NEW ALPHABET according to ALPHABET table and n, which representing n steps movings to produce the NEW ALPHABET.
    """
    n = int(input('Secret number: '))
    s = input('What\'s the ciphered string? ')
    s = upper(s)
    print('The deciphered string is: ' + decipher(n,s))


def upper(s):
    """
    First, we shifted lower cases into upper cases.
    :param s: string
    :return: string, with all upper cases
    """
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if ch.islower():
            ans = ans + ch.upper()
        else:
            ans = ans + ch
    return ans


def decipher(n,s):
    """
    :param n: int, representing moving n steps in ALPHABET table.
    :param s: string, with all upper cases
    :return: string, after deciphered
    """
    decipher1 = ''
    for i in range(len(s)):
        if s[i].isalpha():
            a = new_alphabet(n).find(s[i])
            ch = new_alphabet(n)[a + n]
            decipher1 = decipher1 + ch
        else:
            decipher1 = decipher1 + s[i]
    return decipher1


def new_alphabet(n):
    """
    We create a NEW ALPHABET as new table for deciphering
    :param n: int, representing moving n steps in ALPHABET table.
    """
    new_alphabet = ''
    for i in range(n): # Repeat n times to ensure the new alphabet is long enough
        new_alphabet = new_alphabet + ALPHABET[(26 - n):]
        new_alphabet = new_alphabet + ALPHABET[:(26 - n)]
    return new_alphabet


        # DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
