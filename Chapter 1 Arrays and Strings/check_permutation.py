def check_permutaion(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Two strings are permutation of each other")
    else:
        print("Two strings are not permutation of each other")


input_str1 = input("Enter first string: \n")
input_str2 = input("Enter second string: \n")

check_permutaion(input_str1, input_str2)
