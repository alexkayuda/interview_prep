def decimalToBinary(decimal_num: int) -> str:
    if decimal_num == 0:
        return '0'

    binary_num = ''

    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num

        print(f"{decimal_num} % 2 = {decimal_num % 2} -> {binary_num}")

        decimal_num //= 2

    return binary_num

if __name__ == "__main__":
    numberOne = 12

    print(decimalToBinary(numberOne))