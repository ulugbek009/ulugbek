# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Salom!"))  # "molAS"

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)  # 10 ta Fibonacci sonini chiqaradi



