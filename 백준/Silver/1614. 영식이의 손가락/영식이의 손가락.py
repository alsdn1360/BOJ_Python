# main
hurt_finger = int(input())
finger_use = int(input())

if hurt_finger == 1:
    answer = finger_use * 8
elif hurt_finger == 5:
    answer = finger_use * 8 + 4
else:
    answer = (finger_use // 2) * 8

    if finger_use % 2 == 0:
        answer += hurt_finger - 1
    else:
        answer += 9 - hurt_finger

print(answer)
