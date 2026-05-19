def dailyTemperatures(temperatures: List[int]) -> List[int]:
    st = []
    n = len(temperatures)
    answer = [0] * n

    for i, t in enumerate(temperatures):
        while st and t > temperatures[st[-1]]:
            idx = st.pop()
            print(idx)
            answer[idx] = i - idx
        st.append(i)

    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
