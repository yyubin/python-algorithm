import sys


def time_converter(string):
    min, sec = string.split(':')
    return (int(min) * 60) + int(sec)


s, e, q = map(str, sys.stdin.readline().split())
start = time_converter(s)
end = time_converter(e)
quit = time_converter(q)
start_chat = set()
end_chat = set()

while True:
    try:
        time, nickname = sys.stdin.readline().split()
        time = time_converter(time)
        if time <= start:
            start_chat.add(nickname)
        if end <= time <= quit:
            end_chat.add(nickname)
    except:
        break

count = 0
for i in start_chat:
    if i in end_chat:
        count += 1
print(count)
