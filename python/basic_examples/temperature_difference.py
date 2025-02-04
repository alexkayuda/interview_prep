# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def daily_temp_diff_slow(temperatures : list[int]) -> list[int]:

    if len(temperatures) == 1:
        return [0]

    result = []

    for index, temp in enumerate(temperatures):
        for cursor in range(index + 1, len(temperatures)):
            if temperatures[cursor] > temperatures[index]:
                result.append(cursor - index)
                break
            if cursor == len(temperatures) - 1:
                result.append(0)

    result.append(0)

    return result

def daily_temp_diff_fast(temperatures: list[int]) -> list[int]:
    # Using Monotonic Stack
    # https://www.youtube.com/watch?v=cTBiBSnjO3c

    results = [0] * len(temperatures)
    stack = [] # will hold a pair: [temp, index]
    for index, temperature in enumerate(temperatures):
        while len(stack) > 0 and temperature > stack[-1][0]:
            stackTemperature, stackIndex = stack.pop() # getting [temp, index] from the top of the stack (inserted last)
            results[stackIndex] = index - stackIndex
        stack.append([temperature, index])

    return results

if __name__ == "__main__":
    print(daily_temp_diff_slow([73,74,75,71,69,72,76,73])) # Expected: [1,1,4,2,1,1,0,0]
    print(daily_temp_diff_slow([30,40,50,60])) # Expected: [1,1,1,0]
    print(daily_temp_diff_slow([10])) # Expected: [0]

    print(daily_temp_diff_fast([73, 74, 75, 71, 69, 72, 76, 73]))  # Expected: [1,1,4,2,1,1,0,0]
    print(daily_temp_diff_fast([30, 40, 50, 60]))  # Expected: [1,1,1,0]
    print(daily_temp_diff_fast([10]))  # Expected: [0]

