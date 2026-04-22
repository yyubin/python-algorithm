from collections import defaultdict

def solution(m, musicinfos):

    d = defaultdict(list)
    for idx, musicinfo in enumerate(musicinfos):
        start, end, name, melody = musicinfo.split(",")
        start_hour, start_min = map(int, start.split(":"))
        end_hour, end_min = map(int, end.split(":"))
        start = start_hour * 60 + start_min
        end = end_hour * 60 + end_min
        time = end - start

        last = melody[0]
        melody_list = []
        for i in range(1, len(melody)):
            if melody[i] == "#":
                melody_list.append(last + "#")
                last = ""
            elif last == "":
                last = melody[i]
            else:
                melody_list.append(last)
                last = melody[i]

        if last != "":
            melody_list.append(last)
        if last == "#":
            t = melody_list.pop()
            melody_list.append(t+"#")

        n = len(melody_list)

        if n > time:
            melody = melody_list[:time]
        else:
            mul = time // n
            mod = time % n

            melody = melody_list * mul
            melody += melody_list[:mod]

        d[name] = [time, ','.join(melody)+',', idx]

    able = []

    m_list = []
    last = m[0]
    for i in range(1, len(m)):
        if m[i] == "#":
            m_list.append(last + "#")
            last = ""
        elif last == "":
            last = m[i]
        else:
            m_list.append(last)
            last = m[i]

    if last != "":
        m_list.append(last)
    if last == "#":
        t = m_list.pop()
        m_list.append(t + "#")

    m = ','.join(m_list) + ','

    for key, value in d.items():
        if m in value[1]:
            able.append([key, value[0], value[2]])

    able.sort(key=lambda x: (-x[1], x[2]))

    return "(None)" if len(able) == 0 else able[0][0]

print(solution("ABCDEFG",  	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))