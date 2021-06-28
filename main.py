# pascal

# from math import factorial
# levels = int(input('no. of levels: '))
# for i in range(levels):
#     print(' ' * (levels - i + 1), end="")
#     for j in range(i+1):
#         print(factorial(i)//(factorial(i-j)*factorial(j)), end=" ")
#     print()


# fibonacci
# term = int(input("Enter: "))
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# print(fibonacci(term - 1))

# matrix

x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[1, 2, 3, 9],
     [4, 5, 6, 5],
     [7, 8, 9, 0]]
result = []

if len(x[0]) != len(y):
    print("invalid matrix sizes")

else:
    for i in range(len(y)):
        result.append([0]*len(y[0]))
    for i in range(len(x[0])):
        for j in range(len(y[0])):
            for k in range(len(x[0])):
                result[i][j] += x[i][k] * y[k][j]
print(result)
