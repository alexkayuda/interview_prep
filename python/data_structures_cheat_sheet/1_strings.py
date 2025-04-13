'''
Case Conversion:
upper(): Converts the string to uppercase.
lower(): Converts the string to lowercase.
capitalize(): Capitalizes the first character of the string.
title(): Capitalizes the first character of each word in the string.

Stripping:
strip('char1char2char3'): Removes leading and trailing characters (whitespace by default).
lstrip('char1char2char3'): Removes leading characters (whitespace by default).
rstrip('char1char2char3'): Removes trailing characters (whitespace by default).

Finding and Replacing:
find(sub[, start[, end]]): Returns the lowest index in the string where substring sub is found. Returns -1 if not found.
index(sub[, start[, end]]): Same as find(), but raises a ValueError if the substring is not found.
replace(old, new[, count]): Replaces all occurrences of substring old with new.
count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of substring sub in the range \[start, end].

Splitting and Joining:
split([sep[, maxsplit]]): Splits the string into a list of substrings using sep as the delimiter string.
join(iterable): Concatenates the strings in an iterable with the string as a separator.

Checking:
startswith(prefix[, start[, end]]): Returns True if the string starts with the specified prefix.
endswith(suffix[, start[, end]]): Returns True if the string ends with the specified suffix.
isalpha(): Returns True if all characters in the string are alphabetic.
isalnum(): Returns True if all characters in the string are alphanumeric.
isdigit(): Returns True if all characters in the string are digits.
isspace(): Returns True if all characters in the string are whitespace.

Other methods:
ord(character): Returns the Unicode code point of a one-character string.
chr(integer): Returns the string representing a character whose Unicode code point is the integer.
str(object): Returns a string representation of the object.
ascii(object): Returns a string containing a printable representation of an object, escaping the non-ASCII characters.
'''