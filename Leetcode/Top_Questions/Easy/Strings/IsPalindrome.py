'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

# Solution 1: create an array of chars
# read through string, convert every char to lowercase letter, ignore non-letters, store in array of chars
# check if array of chars == reversed(array of chars)
def isPalindrome_Array(text: str) -> bool:



    return False


#Solution 2: 2 pointers
# create 2 pointers: at the start and at the end of the text
# move them towards the middle, converting all chars to lowercase and ignoring non-letters
# compare each letter on both sides, if not match - not Palindrome
def isPalindrome_Pointers(text: str) -> bool:

    text = text.strip()

    if len(text) == 0 or len(text) == 1:
        return True

    # convert str to a list of chars
    letters = list(text)

    pointer1 = 0
    pointer2 = len(text) - 1

    while pointer1 < pointer2:

        # isalpha() - only letters
        # isalnum() - letters and number
        if not letters[pointer1].isalnum():
            pointer1 += 1
            continue

        if not letters[pointer2].isalnum():
            pointer2 -= 1
            continue

        print(f"Comparing {letters[pointer1]} and {letters[pointer2]}")

        # compare letters
        if letters[pointer1].lower() == letters[pointer2].lower():
            pointer1 += 1
            pointer2 -= 1
            continue
        else:
            # means letters are not the same OR one of them in a digit
            return False
            
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome_Pointers(s)) # true

    s = "race a car"
    print(isPalindrome_Pointers(s)) # false


    s = " "
    print(isPalindrome_Pointers(s)) # true

    s = "0P"
    print(isPalindrome_Pointers(s)) # false

