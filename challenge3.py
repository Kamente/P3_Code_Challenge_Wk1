def is_consonant(char):
    return char.isalpha() and char not in 'aeiou'

def value_of_consonant_substrings(s):
    max_value = 0
    current_value = 0
    
    # for loop to check if the string entered is a consonant
    for char in s:
        if is_consonant(char):
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    return max(max_value, current_value)


input_string = input("Enter a string : ") # prompts user to enter a string
result = value_of_consonant_substrings(input_string)
print(result)
