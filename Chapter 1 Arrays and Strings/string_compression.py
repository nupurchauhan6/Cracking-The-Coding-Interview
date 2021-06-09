def compress_string(input_str):
    if(len(input_str) == 0):
        return "Empty String"
    count = 0
    temp = input_str[0]
    ans = ""
    for index in range(len(input_str)):
        if(temp == input_str[index]):
            count = count + 1
            if(index == len(input_str) - 1):
                ans = ans + temp + str(count)
        else:
            ans = ans + temp + str(count)
            temp = input_str[index]
            count = 1
    return ans


input_str = "aabcccccaaa"

result = compress_string(input_str)
print(result)
