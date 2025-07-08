def operator(op):
    if op == "(":
        return 0
    elif op == "+" or op == "-":
        return 1
    else:
        return 2


# main
notation = input()

postfix = ""
stack = []

for c in notation:
    # 문자열은 바로 postfix에 넣음
    if "A" <= c <= "Z":
        postfix += c
    # 여는 괄호는 무조건 스택에 넣음
    elif c == "(":
        stack.append(c)
    # 닫는 괄호면 여는 괄호가 나올 때까지 연산자를 postfix에 넣음
    elif c == ")":
        while stack[-1] != "(":
            postfix += stack.pop()

        stack.pop()  # ( 버리기
    else:
        while stack and operator(stack[-1]) >= operator(c):
            postfix += stack.pop()

        stack.append(c)

while stack:
    postfix += stack.pop()

print("".join(postfix))
