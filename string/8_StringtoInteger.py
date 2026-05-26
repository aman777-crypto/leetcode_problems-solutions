
def myAtoi(s):

    s = s.strip()


    if not s:
        return 0

  

    sign = 1
    i =0
    result =0

    if s[0] == '-' or s[0] == '+':
        if s[0] =='-':
            sign = -1
        s=s[1:]
    for char in s:
        if not char .isdigit():
            break
        result = result * 10 + int(char)



    result= result  * sign

    if result  < -2**31:
        return -2**31
    elif result > 2**31 -1:
        return 2**31 -1
    return result

new= "  42"
re = myAtoi(new)
print(re)