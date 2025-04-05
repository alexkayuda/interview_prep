from itertools import permutations
from typing import List


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(idx, comb):
        print(f"IDX = {idx}, COMB = {comb}")
        if idx == len(digits):
            res.append(comb[:])
            return

        for letter in digit_to_letters[digits[idx]]:
            print(f"Processing Letter {letter} in [{digit_to_letters[digits[idx]]}]")
            backtrack(idx + 1, comb + letter)

    res = []
    backtrack(0, "")

    return res


if __name__ == "__main__":

    number = "23"
    print(letterCombinations(number)) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]



