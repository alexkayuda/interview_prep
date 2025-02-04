def compress(chars: list[str]) -> int:

    # Case #1:
    if len(chars) == 1:
        #print(f"Case 1: just 1 char. Returning {len(chars)}")
        return len(chars)

    # Case #2:
    if len(chars) == 2:
        #print(f"Case 2: 2 chars. Returning {len(chars)}")
        return len(chars)

    # Case #3:
    counter = 1
    pointer1, pointer2 = 0, 1
    result = 1

    #print(f"I'm gonna loop {len(chars) - 1} times")

    for char in range(0, len(chars) - 1):
        # if chars are the same
        if chars[pointer1] == chars[pointer2]:
            counter += 1
            pointer2 += 1
            continue

        # if chars are different
        else:
            if counter == 1:
                result += 1
            else:
                result += len(str(counter))

        counter = 1
        pointer1 += 1
        pointer2 += 1


    # Case 4: if loop ended but counter > 2
    if counter > 1:
        # calculate the number of digits in the counter
        # append each digit separately
        result += len(str(counter))


    return result

if __name__ == "__main__":

    stringOne = ["a","a","b","b","c","c","c"] # expected 6

    stringTwo = ["a", "b", "c"]

    stringThree = ["a"] # 1
    stringThree = ["a", "a", "a"] # ["a", "3"] -> 2
    stringThree = ["a", "a", "a", "a"] # ["a", "4"] -> 2
    stringThree = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"] # ["a", "1", "2"] -> 3


    #print(compress(stringOne))
    print(compress(stringTwo))
    # print(compress(stringThree))