import math

if __name__ == "__main__":

    original_string = "AbCdEf"
    print(f"Default String: {original_string}")

    print("-" * 25)

    # Ways to reverse String
    # Slicing
    result = original_string[::-1]
    print(f"Reversed String: {result}")

    # Reversed -> creates a new string
    result = "".join(reversed(original_string))
    print(f"Reversed String: {result}")

    # Swapping in-place
    result = list(original_string)
    for i in range(0, int(len(original_string) / 2)): # half of the loop only
        result[i], result[len(original_string) -1 -i] = result[len(original_string) -1 -i], result[i]
    
    result = "".join(result)
    print(f"Reversed String: {result}")

    print("-" * 25)