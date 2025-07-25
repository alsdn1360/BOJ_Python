# main
s = input()
x = input()

stack = []

for c in s:
    if c != x[-1]:
        stack.append(c)
    else:
        temp = []
        is_burn = True

        for x_c in reversed(x[:-1]):
            if stack and x_c == stack[-1]:
                temp.append(stack.pop())
            else:
                is_burn = False
                break

        if not is_burn:
            stack.extend(reversed(temp))
            stack.append(c)

print("".join(stack)) if stack else print("FRULA")
