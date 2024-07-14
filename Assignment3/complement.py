"""
File: complement.py
Name: leo HUNG
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
    This program will help we find the complementary strands of DNA.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))
    # s = input('DNA??')
    # print(build_complement(s))
    # The above two codes are for testing, allowing users to input DNA sequences and automatically generate complementary strands."


def build_complement(dna):
    if dna == '':
        return('DNA strand is missing.')
    else:
        complementary_dna = ''
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                complementary_dna = complementary_dna + 'T'
            if ch == 'T':
                complementary_dna = complementary_dna + 'A'
            if ch == 'C':
                complementary_dna = complementary_dna + 'G'
            if ch == 'G':
                complementary_dna = complementary_dna + 'C'
        return complementary_dna



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
