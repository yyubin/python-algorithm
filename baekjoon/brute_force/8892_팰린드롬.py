cnt = int(input())

while cnt > 0:
    cnt2 = int(input())
    strings = []

    for _ in range(cnt2):
        strings.append(input())

    result = ""
    for i in strings:
        if i == i[::-1]:
            result = i
            break
    print(result if result != "" else 0)

