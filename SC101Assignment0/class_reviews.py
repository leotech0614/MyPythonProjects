"""
File: class_reviews.py
Name: leo HUNG
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1


def main():
    """
    This program help us calculate the final exam score of class SC001 and SC101.
    We may first input which class we would like to know and the score, and the program will help us find the Max, min and Avg.
    We can input '-1' to show the final reult.
    """
    Class = input('Which class? ')
    Class = upper(Class)

    if Class == str(EXIT):
        print('No class scores were entered')

    else:
        if 'SC001' or 'SC101' in Class:
            S = int(input('Score: '))

            if 'SC001' in Class:
                maximum0 = S
                minimum0 = S
                datas0 = S
                number0 = 1
            else:
                maximum0 = 0
                minimum0 = 0
                datas0 = 0
                number0 = 0

            if 'SC101' in Class:
                maximum1 = S
                minimum1 = S
                datas1 = S
                number1 = 1
            else:
                maximum1 = 0
                minimum1 = 0
                datas1 = 0
                number1 = 0

            while True:
                Class = input('Which class? ')
                Class = upper(Class)

                if 'SC001' in Class:
                    S0 = int(input('Score: '))
                    datas0 += S0
                    number0 += 1
                    if number0 == 1 and number1 != 0:
                        maximum0 = S0
                        minimum0 = S0
                    if S0 > maximum0:
                        maximum0 = S0
                    if S0 < minimum0:
                        minimum0 = S0
                if 'SC101' in Class:
                    S1 = int(input('Score: '))
                    datas1 += S1
                    number1 += 1
                    if number1 == 1 and number0 != 0:
                        maximum1 = S1
                        minimum1 = S1
                    if S1 > maximum1:
                        maximum1 = S1
                    if S1 < minimum1:
                        minimum1 = S1
                if Class == str(EXIT):
                    break

            print('=============SC001=============')
            if number0 == 0:
                print('No data for SC001')
            else:
                Data0 = float((datas0/number0))
                print('Max(001): ' + str(maximum0))
                print('Min(001): ' + str(minimum0))
                print('Avg(001): ' + str(Data0))
            print('=============SC101=============')
            if number1 == 0:
                print('No data for SC101')
            else:
                Data1 = float((datas1 / number1))
                print('Max(101): ' + str(maximum1))
                print('Min(101): ' + str(minimum1))
                print('Avg(101): ' + str(Data1))


def upper(Class):
    ans = ''
    for i in range(len(Class)):
        a = Class[i]
        if a.islower():
            ans = ans + a.upper()
        else:
            ans = ans + a
    return ans


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
