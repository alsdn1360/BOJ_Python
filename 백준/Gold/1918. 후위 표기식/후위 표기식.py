# main
notation = input()

postfix = []
stack = []

for c in notation:
    # 문자열은 바로 postfix에 넣음
    if 65 <= ord(c) <= 90:
        postfix.append(c)
    else:
        # 여는 괄호는 무조건 스택에 넣음
        if c == "(":
            stack.append(c)
        # 닫는 괄호면 여는 괄호가 나올 때까지 연산자를 postfix에 넣음
        elif c == ")":
            while stack:
                if stack[-1] == "(":
                    stack.pop()
                    break

                postfix.append(stack.pop())
        else:
            if not stack:
                stack.append(c)
            else:
                # 스택 top보다 우선순위가 높은 연산자면 스택에 넣음
                if c == "*" or c == "/":
                    if stack[-1] == "(" or stack[-1] == "+" or stack[-1] == "-":
                        stack.append(c)
                    else:
                        # 낮은 우선순위가 나올 때까지 계속 postfix에 넣음
                        while stack:
                            if stack[-1] == "(" or stack[-1] == "+" or stack[-1] == "-":
                                break

                            postfix.append(stack.pop())

                        stack.append(c)
                else:
                    # '+', '-' 보다 낮은 우선순위는 괄호밖에 없음
                    while stack:
                        if stack[-1] == "(":
                            break

                        postfix.append(stack.pop())

                    stack.append(c)

while stack:
    postfix.append(stack.pop())

print("".join(postfix))
