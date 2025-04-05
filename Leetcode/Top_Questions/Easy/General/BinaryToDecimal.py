def binaryToDecimal(binary: str) -> int:

    result = 0
    binary_list = list(binary) # ['1','0','0','1']


    for i, element in enumerate(range(len(binary_list) - 1, -1, -1)):
        calculation = (int(binary_list[len(binary_list) - 1 -i]) * pow(2, i))
        #print(f"{int(binary_list[len(binary_list) - 1 - i])} * 2^{i} = {calculation}")

        result += calculation

    return result

if __name__ == "__main__":

    binaryOne = "10011" # 19
    binaryTwo = "10011000111" # 1223

    print(binaryToDecimal(binaryOne))
    print(binaryToDecimal(binaryTwo))