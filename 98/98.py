import csv
from collections import defaultdict
from math import sqrt
from itertools import combinations, permutations

def parse_file():
    with open('words.txt', 'rb') as f:
        reader = csv.reader(f)
        words = list(reader)[0]
    return words

def get_anagrams(words):
    word_dict = defaultdict(list)
    for w in words:
        sorted_w = ''.join(sorted(w))
        word_dict[sorted_w].append(w)
    anagrams = {''.join(set(k)):v for (k,v) in word_dict.iteritems() if len(v)>1}
    return anagrams


def is_square(n):
    root = sqrt(n)
    return root == int(root)


def sub(key, nums, words):
    vals = []
    fn = lambda L: nums[key.index(L)]

    for word in words:
        val = ''.join(map(fn, word))
        if val[0] != '0':
            yield int(val)


def main():
    words = parse_file()
    anagrams = get_anagrams(words)

    digits = '0123456789'
    max_sq = 0
    for key, words in anagrams.iteritems():
        for nums in permutations(digits, len(key)):
            vals = sub(key, nums, words)

            sqs = [v for v in vals if is_square(v)]
            if len(sqs) > 1:
                max_sq = max(max_sq, max(sqs))
    return max_sq


words = parse_file()
anagrams = get_anagrams(words)
print main()
