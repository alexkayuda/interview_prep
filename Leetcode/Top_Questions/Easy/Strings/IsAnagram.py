'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Anagrams are words that are formed by rearranging the letters of another word or phrase, 
using all the original letters exactly once.

"listen" and "silent" are anagrams of each other because both words use the same letters in a different order.

 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

def isAnagram(s: str, t: str) -> bool:

    # edge case
    if len(s) != len(t):
        return False

    letters = {}

    for letter in s:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] = letters[letter] + 1

    for letter in t:
        if letter not in letters or letters[letter] == 0:
            return False
        else:
            letters[letter] = letters[letter] - 1

    return True

if __name__ == "__main__":

    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t)) # True

    s = "rat"
    t = "car"
    print(isAnagram(s,t)) # False