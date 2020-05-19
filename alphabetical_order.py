from math import factorial as fact


# Find number of remaining smaller
def smaller_char(st, ind):
    count = 0
    i = ind + 1
    while i < len(st):
        if st[i] < st[ind]:
            count += 1
        i += 1
    return count


# Find factorial of remaining duplicates
def duplicates(st):
    new_st = ''
    for char in st:
        if char not in new_st:
            new_st += char
    num = len(st) - len(new_st)
    return 2**num


def word_rank(word):
    rank = 1
    for i in range(len(word)):
        dup = duplicates(word[i:])
        small = smaller_char(word, i)
        rank += (small * fact(len(word)-i-1))/dup
    return int(rank)


string = input('Enter a word: ')
print(word_rank(string))
