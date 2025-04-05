'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

 
Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        if x == y:
            return 0

        difference = 0
        
        # convert X and Y to binary 
        # and store as a list 
        # remove out '0b' prefix (it's important!) -> originally, it stores it as "0b1001"
        # make that list 32 chars and fill the empty ones with 0
        bin_x = [bit for bit in bin(x)[2:].zfill(32)]
        bin_y = [bit for bit in bin(y)[2:].zfill(32)]

        # print(bin_x)
        # print(bin_y)

        for i in range(32):
            if bin_x[len(bin_x) - 1 -i] == bin_y[len(bin_y) - 1 -i]:
                continue
            else:
                difference += 1

        return difference


class HammingDistance:

    obj = Solution()

    x = 1
    y = 4
    print(obj.hammingDistance(x,y)) # 2

    x = 3
    y = 1
    print(obj.hammingDistance(x,y)) # 1

    x = 10
    y = 7
    print(obj.hammingDistance(x,y)) # 3

    x = 4
    y = 14
    print(obj.hammingDistance(x,y)) # 2
