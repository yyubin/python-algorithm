from collections import defaultdict

def solution(m, musicinfos):

    d = defaultdict(list)
    for i, musicinfo in enumerate(musicinfos):
        start, end, name, melody = musicinfo.split(",")
        start_hour, start_min = map(int, start.split(":"))
        end_hour, end_min = map(int, end.split(":"))
        start = start_hour * 60 + start_min
        end = end_hour * 60 + end_min
        time = end - start

        n = len(melody)
        tmp = time // n
        if time % n != 0:
            tmp += 1

        d[name] = [time, melody*tmp, i]

    able = []

    for key, value in d.items():
        if m in value[1]:
            if m[-1] != "#" and m + "#" in value[1]:
                value[1].replace(m[-2]+"#", "")
                if m in value[1]:
                    able.append([key, value[0], value[2]])
            else:
                able.append([key, value[0], value[2]])

    print(d)
    able.sort(key=lambda x: (-x[1], x[2]))
    print(able)


    answer = ''
    return answer

print(solution("ABCDEFG",  	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))