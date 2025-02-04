def int_to_string(value: int) -> str:

    result = None

    try:
        result = chr(value)
    except ValueError:
        print(f"Valid input integers range is from 0 to 127. You have entered {value}")

    return result

def string_to_int(character: str) -> int:
    return ord(character)

if __name__ == "__main__":
    value = None
    result = int_to_string(value)
    print(f"{value} is corresponds to {result}. {result} is of type {type(result)}")

    character = "B"
    result = string_to_int(character)
    print(f"{value} is corresponds to {result}. {result} is of type {type(result)}")