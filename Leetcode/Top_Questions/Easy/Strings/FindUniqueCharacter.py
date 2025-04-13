'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

'''
from collections import OrderedDict

def firstUniqChar(s: str) -> int:
    
    letters = OrderedDict()

    # convert str to list of char
    char_list = list(s)

    for index, letter in enumerate(char_list):
        if letter not in letters:
            letters[letter] = [index]
        else:
            letters[letter].append(index)

    for key, value in letters.items():
        if len(value) == 1:
            return letters[key][0]

    return -1

if __name__ == "__main__":
    s = "leetcode"
    print(firstUniqChar(s)) # 0

    s = "loveleetcode"
    print(firstUniqChar(s)) # 2

    s = "aabb"
    print(firstUniqChar(s)) # -1