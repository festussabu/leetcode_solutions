def generateParenthesis(n: int) -> List[str]:

    stack = []
    res = []
    def backtracking(open_, close_):
        if open_ == close_ == n:
            res.append("".join(stack))
            return

        if open_ < n:
            stack.append("(")
            backtracking(open_ + 1, close_)
            stack.pop()

        if close_ < open_:
            stack.append(")")
            backtracking(open_, close_ + 1)
            stack.pop()

    backtracking(0, 0)
    return res

n = 3
print(generateParenthesis(n))

