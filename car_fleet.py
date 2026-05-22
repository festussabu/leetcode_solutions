def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p, t] for p, t in zip(position, speed)]
    st = []
    for p, s in sorted(pair)[::-1]:
        st.append((target - p)/s)
        if len(st) >= 2 and st[-1] <= st[-2]:
            st.pop()
    return len(st)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))
