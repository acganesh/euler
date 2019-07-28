# Notes
# Write a main function that iterates through the possibilities,
# and backtracks if a contradiction is found.
# Analogous to the recursive backtracing sudoku algorithm.

# A tuple of lists of the form [val, places], where
# val: the value of the guess
# places: the number of places the guess contained the correct digit

import itertools
import time

guesses = (['90432', 2], ['39458', 2], ['51545', 2], ['34109', 1],
           ['12531', 1], ['70794', 0])


def search(guesses, candidates):
    candidates = {}

    for guess in guesses:
        val = guess[0]
        length = len(val)
        places = guess[1]

        for indices in itertools.combinations(range(length), places):
            for ind in indices:
                if not (ind in candidates.keys()):
                    candidates[ind] = val[ind]
                    break
        print candidates
        time.sleep(0.1)

    return main(guesses, candidates)
