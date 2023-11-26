Positive Integer Extractor
Description
The Positive Integer Extractor is a Python utility designed to extract positive integers from a list of strings. It is particularly useful in data processing where inputs are mixed with various data types and formats, and there's a need to selectively parse and use positive integer values.

Features
Type Checking: Ensures that the input is a list of strings, raising a TypeError otherwise.
Integer Extraction: Iterates through the list and extracts strings that are positive integers.
Validation: Checks if all elements that appear as digits are positive integers, raising a ValueError for any discrepancies.
Usage
To use this utility, simply import the function and pass a list of strings to it. Example usage is as follows:

python
Copy code
from extract_positive_integers import extract_positive_integers

input_list = ["123", "456", "-7", "789", "abc", "12.34"]
result = extract_positive_integers(input_list)
print(result)  # Output will be [123, 456, 789]
Requirements
This script requires Python 3.x.

Installation
No installation is required. Just download extract_positive_integers.py


# john_2023_AT6
