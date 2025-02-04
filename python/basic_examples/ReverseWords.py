import math


def reverseWords(s: str) -> str:
    if len(s) == 1:
        return s

    words = s.split()

    for i in range(0, math.floor(len(words) / 2)):
        words[i], words[len(words) - 1 - i] = words[len(words) - 1 - i].strip(), words[i].strip()

    # print(" ".join(words))
    return " ".join(words)

if __name__ == "__main__":
    if reverseWords("a good   example") == "example good a":
        print("Good! Solved by: reverseWords")
    else:
        print("Something is wrong")