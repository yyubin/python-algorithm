# sys.stdin.readline은 EOFError시 공백반환함
while True:
    try:
        n = int(input().rstrip())
    except EOFError:
        break

    if n == 1:
        print('1')
        continue

    num = 1
    cnt = 0
    while True:
        num = num * 10 + 1
        cnt += 1
        if num % n == 0:
            print(cnt)
            break
        num += 1

