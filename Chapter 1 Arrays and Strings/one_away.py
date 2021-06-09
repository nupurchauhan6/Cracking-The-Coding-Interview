def is_one_away(str1, str2):
    diff = len(str1) - len(str2)
    if diff == 0:
        # check for replace
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count = count + 1
            if count > 1:
                return False
        return True
    elif diff == 1:
        # check for remove
        print("remove")
    elif diff == -1:
        # check for insert
        print("insert")
    return False


str1 = "pale"
str2 = "ple"

print(is_one_away(str1, str2))
