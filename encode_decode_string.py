def encode(strs: List[str]) -> str:
    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    print(result)
    return result


def decode(s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = s.find('#', i)        # find delimiter
        length = int(s[i:j])      # number before #

        start = j + 1
        end = start + length

        result.append(s[start:end])
        i = end                   # jump forward

    return result

dummy_input = ["Hello","World"]
dummy_input = ['"']
encoded_string = encode(dummy_input)
print(decode(encoded_string))
