print("hello")

def reverse(a) -> 123:
    rev = 0
    while a:
        mod = a % 10
        a //= 10
        rev = rev * 10 + mod

    return rev

res = reverse(431)
print(res)