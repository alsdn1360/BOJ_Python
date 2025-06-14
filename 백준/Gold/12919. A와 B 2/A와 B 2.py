# T에서 S로 만들어감
def bt(str):
    if str == s:
        return 1

    if len(str) <= len(s):
        return 0

    # 1번 조건: 문자열 뒤에 A를 추가했으니, 문자열 끝이 A이면 끝에 있는 A를 제거
    if str[-1] == "A":
        if bt(str[: len(str) - 1]):
            return 1

    # 2번 조건: 문자열 뒤에 B를 추가하고 뒤집었으니, 문자열 앞이 B이면 앞에 있는 B를 제거하고 뒤집기
    if str[0] == "B":
        if bt("".join(reversed(str[1:]))):
            return 1

    return 0


# main
s = input()
t = input()

print(bt(t))
