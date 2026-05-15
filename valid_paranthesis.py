def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    st = []
    for i in range(len(s)):
        if s[i] in "([{":
            st.append(s[i])
        else:
            if not st:
                return False
            top = st.pop()
            if s[i] == ')' and  top != '(' or s[i] == '}' and  top != '{' or s[i] == ']' and  top != '[':
                return False
    if len(st) > 0:
        return False
    else:
        return True

s = "([)]"
s = "([])"
print(isValid(s))
