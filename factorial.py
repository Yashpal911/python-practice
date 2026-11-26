def factorial(n):
    for x in range(1, n):
        n = n * x
    return n 

def re_fact(n):
    if n == 0:
        return 1
    else:
        return n * re_fact(n - 1)

print(factorial(3))
print(re_fact(3))