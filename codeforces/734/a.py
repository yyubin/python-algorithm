import sys
for _ in range(int(sys.stdin.readline())):
    money = int(sys.stdin.readline())
    if money%3 == 2:
        print(money//3, (money//3)+1)
    elif money%3 == 1:
        print((money//3)+1, money//3)
    else:
        print(money//3, money//3)

