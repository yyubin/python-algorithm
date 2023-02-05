def up_down_left_right(n:int, string:str):
    li = list(string.split())
    dx = (0, -1, 0, 1)
    dy = (1, 0, -1, 0)
    dic = {'R' : 0, 'U' : 1, 'L' : 2, 'D' : 3}
    x = 1
    y = 1
    for v in li:
        temp = dic[v]

        if n >= (x + dx[temp]) >= 1 and n >= (y + dy[temp]) >= 1:
            x += dx[temp]
            y += dy[temp]

    return x, y
# print(up_down_left_right(5, "R R R U D D"))

def time(hour:int):
    result = 0
    hou = 0
    min = 0
    sec = 0

    while hou != (hour+1):
        min += 1
        if min == 60:
            min = 0
            sec += 1
            if sec == 60:
                sec = 0
                hou += 1
        if (str(hou)+str(min)+str(sec)).find('3') != -1:
            result += 1
    return result
# print(time(5))

def time2(hour:int):
    count = 0
    for i in range(hour+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    return count
# print(time2(5))

def knight(place:str):
    li = list(place)

    dx = (2, 2, -2, -2, 1, -1, 1, -1)
    dy = (1, -1, 1, -1, 2, 2, -2, -2)
    dic = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,
           'e' : 5,'f' : 6, 'g' : 7, 'h' : 8}

    result = 0

    x = dic[li[0]]
    y = int(li[1])

    for i in range(8):
        if 8 >= (x + dx[i]) >= 1 and 8 >= (y + dy[i]) >= 1:
            result += 1

    return result

# print(knight('a1'))

def restring(string:str):
    li = list(string)

    li1 = [i for i in li if ord(i) >= 65]
    li1.sort()

    li2 = [int(i) for i in li if ord(i) < 65]
    number = sum(li2)

    print(*[i for i in li1], sep="", end="")
    print(number)

print(restring("K1KA5CB7"))





