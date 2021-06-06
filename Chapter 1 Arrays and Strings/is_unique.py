def is_unique(input_str):
    char_set = [False]*128
    for char in input_str:
        index = ord(char)
        if char_set[index]:
            return "The string has duplicate characters!"
        else:
            char_set[index] = True
    return "The string does not have duplicate characters!"


input_str = input("Enter a string: \n")

output_str = is_unique(input_str.lower())

print(output_str)
