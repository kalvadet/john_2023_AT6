def extract_positive_integers(strings):
    if not isinstance(strings, list):
        raise TypeError("Input should be a list of strings")

    positive_integers = []

    for string in strings:
        if string.isdigit():
            positive_integers.append(int(string))

    if len(positive_integers) != len([s for s in strings if s.isdigit()]):
        raise ValueError("Not all elements in the new list are valid positive integers")

    return positive_integers

# Example usage:
input_list = ["123", "456", "-7", "789", "abc", "12.34"]
result = extract_positive_integers(input_list)
print(result)  
