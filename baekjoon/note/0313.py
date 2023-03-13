while True:
    string = input()
    if string == '#':
        break
    string = string.lower()
    res = 0
    res += string.count('a')
    res += string.count('e')
    res += string.count('i')
    res += string.count('o')
    res += string.count('u')
    print(res)