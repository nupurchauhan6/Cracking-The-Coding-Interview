def string_rotation(str1, str2):
    first = str1[0]
    index = 0
    for i in range(len(str2)):
        if str2[i] == first:
            index = i
    return False


str1 = "waterbottle"
str2 = "erbottlewat"

print(string_rotation(str1, str2))
