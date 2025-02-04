# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Input: s = "leetcode"
#
# Output: "leotcede"


vowels = ('a', 'e', 'i', 'o', 'u')

def reverseVowelsInPlace(s: str) -> str:
    if len(s) == 1:
        return s

    # IMPORTANT: Cool trick to convert String to Char Array
    word = list(s)

    start, end = 0, len(s) - 1

    print(word)
    while start < end:

        # move start pointer forward until it finds a vowel or meets the end pointer
        while start < end and word[start].lower() not in vowels:
            start += 1
            print(f"Start Pointer found a vowel at position {start}")


        # move end pointer backwards until it finds a vowel or meets the start pointer
        while start < end and word[end].lower() not in vowels:
            end -= 1
            print(f"End Pointer found a vowel at position {end}")

        # swap vowels
        print(f"Swapping {word[start]} with {word[end]}")
        word[start], word[end] = word[end], word[start]

        start += 1
        end -= 1

    # convert list or characters into string
    print(word)
    return "".join(word)

def reverseVowelsStack(s: str) -> str:

    if len(s) == 1:
        return s

    stackOfVowels = []  # pair: [vowel, index]
    result = ""

    for index, char in enumerate(s):
        if char.lower() in vowels:
            stackOfVowels.append([char, index])

    for index, char in enumerate(s):
        if char.lower() in vowels:
            result += stackOfVowels[-1][0]
            stackOfVowels.pop()
            continue
        result += char

    return result


if __name__ == "__main__":
    if reverseVowelsInPlace("leEtcode") == "leotcEde":
        print("Good! Solved by: reverseVowelsInPlace")
    else:
        print("Something is wrong")

    if reverseVowelsStack("leEtcode") == "leotcEde":
        print("Good! Solve by: reverseVowelsStack")
    else:
        print("Something is wrong")