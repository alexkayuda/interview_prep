'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
haystack and needle consist of only lowercase English characters.

 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

# Option 1
def strStr(haystack: str, needle: str) -> int:
        return haystack.find(needle)


def strStr(self, haystack: str, needle: str) -> int:
        return -1

if __name__ == "__main__":
