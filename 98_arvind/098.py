from collections import defaultdict
from pprint import pprint
import itertools

import math
def isAnagram(num1, num2):
    return sorted(num1) == sorted(num2) and num1 != num2

def isPerfectSquare(num):
    return math.sqrt(num) == int(math.sqrt(num))

def digitize(num):
    power =  len(num) - 1
    s = 0
    for val in num:
        val = int(val)
        s += val * 10 ** power
        power -= 1
    return s

def mapWord(word, number):
    dictionary = {}
    if len(word) != len(number):
        return False
    for x in xrange(len(word)):
        dictionary[word[x]] = number[x]
    return dictionary

def remap(dict, word):
    w = ""
    for letter in word:
        w += dict[letter]
    return w

with open("words.txt", "r") as f:
    text = f.readlines()
    arr = []
    for line in text:
        line = line.rstrip("\n")
        line = line.replace('"', "")
        arr = line.split(",")

anagramDict = defaultdict(list)

"""
for word in arr:
    word_s = ''.join(sorted(word))
    anagramDict[word_s].append(word)
"""

for word in arr:
    for word2 in arr:
        if len(word) != len(word2):
            continue
        if isAnagram(word, word2) and word2 not in anagramDict:
            anagramDict[word].append(word2)

anagramList = []
for key, value in anagramDict.iteritems():
    tup = (key, value[0])
    if len(value) == 2:
        tup = (key, value[0], value[1])
    anagramList.append(tup)

import pdb; pdb.set_trace()


digits = '0123456789'
lst = []
# Iterate through word lengths
for x in xrange(3, 10):
    word_len = x
    for subs in itertools.permutations(digits, word_len):
        if subs[0] == '0':
            continue
        dig = digitize(subs)
        if not isPerfectSquare(dig):
            continue
        for pair in anagramList:
            for perm in itertools.permutations(str(dig), len(str(dig))):
                digperm = digitize(perm)
                if not isPerfectSquare(digperm):
                    continue
                if pair[0] != len(str(digperm)):
                    break
                mapdict = mapWord(pair[0], str(dig))
                if remap(mapdict, pair[1]) == str(digperm):
                    print digperm, dig


square_dict = defaultdict(list)
for word in lst:
    for word2 in lst:
        if len(word) != len(word2):
            continue
        if isAnagram(word, word2) and word2 not in square_dict:
            square_dict[word].append(word2)
