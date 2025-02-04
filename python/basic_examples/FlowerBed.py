# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule
# and false otherwise.
#

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:

    # if we don't need to plant anything - we are done
    if n == 0:
        return True

    # Case 1: flowerbed size = 1
    if len(flowerbed) == 1:
        if n > 1:
            return False
        else:
            return True if flowerbed[0] == 0 else False

    # Case 2: flowerbed size = 2
    if len(flowerbed) == 2:
        if n > 1:
            return False
        else:
            if flowerbed[0] != 0 or flowerbed[1] != 0:
                return False
            else:
                return True

    # Case 3: Edge Cases:
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    if flowerbed[-2] == 0 and flowerbed[-1] == 0:
        flowerbed[-1] = 1
        n -= 1

    # Case 4: Everything Else
    for spot in range(1, len(flowerbed) - 1):
        if flowerbed[spot - 1] == 0 and flowerbed[spot] == 0 and flowerbed[spot + 1] == 0:
            n -= 1
            flowerbed[spot] = 1

    return True if n <= 0 else False

if __name__ == "__main__":
    print(canPlaceFlowers([1,0,0,0,1], 1)) # True
    print(canPlaceFlowers([0,0,1,0,1], 1)) # True
    print(canPlaceFlowers([1,0,0,0,1], 1))

