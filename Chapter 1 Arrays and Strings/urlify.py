def urlify(input_str, true_len):
    ans = ""
    for index in range(true_len):
        if input_str[index] == ' ':
            ans = ans + "%20"
        else:
            ans = ans + input_str[index]
    print(ans)


input_str = "Mr John Smith    "
true_length = 13
print(input_str, true_length)

urlify(input_str, true_length)
