# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 2 is written as II
# 12 is written as XII
# 27 is written as XXVII

roman_symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romanToInt(s: str) -> int:

    result = 0

    for index in range(len(s)):
        # if the next symbol is larger than the current one, then we need to subtract
        if index < len(s) - 1 and roman_symbols[s[index]] < roman_symbols[s[index + 1]]:
            result -= roman_symbols[s[index]]
        else:
            result += roman_symbols[s[index]]

    return result


if __name__ == "__main__":


    print(romanToInt("MCMXCIV")) # 1994