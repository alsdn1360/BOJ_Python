def check_fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


# main
inputs = []

for _ in range(3):
    inputs.append(input())

for i, inp in enumerate(inputs):
    if inp.isdigit():
        idx = int(inp) + (3 - i)
        break

print(check_fizz_buzz(idx))
