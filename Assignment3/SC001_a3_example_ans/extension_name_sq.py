"""
File: name_sq.py (extension)
Name: Example Answer
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name,
and the square pattern of the given
name will be printed on the console.
"""


def main():
    """
    This program will print a square pattern of the given
    name provided by the user.
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    name_square(name)


def name_square(name):
    """
     :param name: str, the name to be printed in a square pattern.
    """
    for i in range(len(name)):
        if i == 0:
            print(name)
        elif i == len(name) - 1:
            for j in range(len(name)):
                print(name[len(name) - 1 - j], end='')
            print('')
        else:
            for j in range(len(name)):
                if j == 0:
                    print(name[i], end='')
                elif j == len(name) - 1:
                    print(name[len(name) - 1 - i])
                else:
                    print(' ', end='')


# --- DO NOT EDIT CODE BELOW THIS LINE --- #
if __name__ == '__main__' :
    main()
