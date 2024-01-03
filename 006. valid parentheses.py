# Created via GPT
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

# sample
s = "()[]{}"
result = isValid(s)
print(result)  # output True
