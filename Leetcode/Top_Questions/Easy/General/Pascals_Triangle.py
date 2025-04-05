'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


n = 6
                1                    1 
               1 1                   1 1
              1 2 1                  1 2 1
             1 3 3 1        ==>>     1 3 3 1
            1 4 6 4 1                1 4 6 4 1
          1 5 10 10 5 1              1 5 10 10 5 1
'''

from typing import List

class Solution:
    def generate_using_recursion(self, numRows: int) -> List[List[int]]:

        # Define Base Cases
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        # get to the base case using recursion
        prevRows = self.generate_using_recursion(numRows - 1)

        # get the latest rows
        prevRow = prevRows[-1]

        # create a new row
        currentRow = []

        # append 1 to the beggining
        currentRow.append(1)

        # append sums of elements
        for i in range(1, numRows - 1):
            currentRow.append(prevRow[i-1] + prevRow[i])

        # append 1 to the end
        currentRow.append(1)

        # "include" newly built row to the list of all rows
        prevRows.append(currentRow)

        return prevRows

    def generate_using_combinatorial(self, numRows: int) -> List[List[int]]:

        # edge case
        if numRows == 0:
            return []

        # to store all rows
        result = []

        # create first row and add to result list
        firstRow = []
        firstRow.append(1)
        result.append(firstRow)

        # we will get into this loop ONLY if numRows > 1 (e.g., 2,3,4...)
        for i in range(1, numRows):
            
            # get previous row
            prevRow = result[-1]

            # create a new row
            newRow = []

            # add 1 to the beginning of a new row
            newRow.append(1)

            # calculate the sum or 2 number from the row above
            for j in range(1, i):
                newRow.append(prevRow[j-1] + prevRow[j])

            # add 1 to the END of a new row
            newRow.append(1)

            # add new row to result
            result.append(newRow)
        
        return result



class PascalsTriangle:

    obj = Solution()

    n = 2
    print(obj.generate_using_recursion(n)) # [ [1], [1,1] ]

    n = 3
    print(obj.generate_using_recursion(n)) # [ [1], [1,1], [1,2,1] ]

    n = 4
    print(obj.generate_using_recursion(n)) # [ [1], [1,1], [1,2,1], [1,3,3,1] ]

    print("-" * 20)

    n = 2
    print(obj.generate_using_combinatorial(n)) # [ [1], [1,1] ]

    n = 3
    print(obj.generate_using_combinatorial(n)) # [ [1], [1,1], [1,2,1] ]

    n = 4
    print(obj.generate_using_combinatorial(n)) # [ [1], [1,1], [1,2,1], [1,3,3,1] ]
