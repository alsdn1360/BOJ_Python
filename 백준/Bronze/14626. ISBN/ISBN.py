# main
isbn = input()

m = int(isbn[-1])

broken_idx = 0
temp_total = 0

for i in range(12):
    if isbn[i] == "*":
        broken_idx = i
        continue

    if i % 2 != 0:
        temp_total += 3 * int(isbn[i])
    else:
        temp_total += int(isbn[i])

if broken_idx % 2 != 0:
    for broken_num in range(10):
        total = temp_total + 3 * broken_num + m

        if total % 10 == 0:
            print(broken_num)
            break
else:
    for broken_num in range(10):
        total = temp_total + broken_num + m

        if total % 10 == 0:
            print(broken_num)
            break
