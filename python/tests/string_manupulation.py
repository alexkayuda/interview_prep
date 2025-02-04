import math

if __name__ == "__main__":

    original_string = "AbCdEf"
    print(f"Default String: {original_string}")

    print("-" * 25)

    # Ways to reverse String
    # Slicing
    result = original_string[::-1]
    print(f"Reversed String: {result}")

    # Reversed
    result = "".join(reversed(original_string))
    print(f"Reversed String: {result}")

    # Looping and swapping
    result = list(original_string)
    for index in range(0, math.floor(len(original_string) / 2)): # half of the loop only
        result[index], result[len(original_string) - 1] = result[len(original_string) - 1], result[index]
    result = "".join(result)
    print(f"Reversed String: {result}")

    print("-" * 25)