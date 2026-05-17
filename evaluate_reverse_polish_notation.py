def evalRPN(tokens: List[str]) -> int:
    st = []
    for i in range(len(tokens)):
        if tokens[i] == '+':
            if st and len(st) >= 2:
                b = st.pop()
                a = st.pop()
                st.append(int(a + b))
        elif tokens[i] == '-':
            if st and len(st) >= 2:
                b = st.pop()
                a = st.pop()
                st.append(int(a - b))
        elif tokens[i] == '*':
            if st and len(st) >= 2:
                b = st.pop()
                a = st.pop()
                st.append(int(a * b))
        elif tokens[i] == '/':
            if st and len(st) >= 2:
                b = st.pop()
                a = st.pop()
                st.append(int(a / b))
        else:
            st.append(int(tokens[i]))
    return st.pop()


tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
