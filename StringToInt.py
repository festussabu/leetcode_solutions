def myAtoi(s: str) -> int:
    INT_MIN = -2147483648  # -2^31
    INT_MAX =  2147483647  #  2^31 - 1
    sign = 1
    result = 0

    # Step 1: Skip leading whitespace
    s = s.strip()

    if not s:
        return 0

    # Step 2: Determine sign
    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            sign = -1
        s = s[1:]

    # Step 3: Read digits (leading zeros are naturally handled)
    for char in s:
        if not char.isdigit():
            break
        result = result *10 + int(char)


    result *= sign

    # Step 4: Clamp to 32-bit signed integer range
    if result < -2**31:
        return -2**31
    elif result > 2**31-1:
        return 2**31 - 1
    return result


s = "42"
s = " "
print(myAtoi(s))
