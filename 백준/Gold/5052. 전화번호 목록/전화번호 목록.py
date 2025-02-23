t = int(input())

for i in range(t):
    consistency = True

    n = int(input())
    phone_book = [input() for _ in range(n)]
    phone_book.sort()

    for j in range(len(phone_book) - 1):
        if phone_book[j + 1].startswith(phone_book[j]):
            consistency = False
            break

    if consistency:
        print('YES')
    else:
        print('NO')
