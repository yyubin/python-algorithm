# a, b = map(int, input().split())
# print(a+b)

# print(ord(input()))

# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

a = int(input())

for i in range(a):
    for j in range(a):
        print(" " * (i % 2), end="")
        print("*", end="")
        if i%2 == 0:
            print(" " * ((i % 2) +1), end="")
    print()