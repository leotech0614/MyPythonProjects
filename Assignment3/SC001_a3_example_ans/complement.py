"""
File: complement.py
Name: Example Answer
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program will use string manipulation
    to find the complement strand of given DNA sequences  .
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, the template used to make a complement ssDNA sequence.
    :return ans: str, the complement ssDNA sequence.
    """
    if len(dna) == 0:
        return 'DNA strand is missing'
    else:
        ans = ''
        for ch in dna:
            if ch == 'A':
                ans += 'T'
            elif ch == 'T':
                ans += 'A'
            elif ch == 'C':
                ans += 'G'
            else:
                ans += 'C'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
