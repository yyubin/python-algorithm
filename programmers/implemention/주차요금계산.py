from collections import defaultdict

def solution(fees, records):
    d = defaultdict(list)

    for record in records:
        re = record.split()
        time = list(map(int, re[0].split(":")))
        d[re[1]].append((re[-1], time))

    for number, data in d.items():
        if data[-1][0] == "IN":
            d[number].append(('OUT', [23, 59]))

    res = defaultdict(int)
    for number, data in d.items():
        in_hour, in_minute = 0, 0

        for type, time in data:
            if type == "IN":
                in_hour = time[0]
                in_minute = time[1]
                continue

            else:
                use_time = (time[0] - in_hour) * 60 + time[1] - in_minute
                res[number] += use_time
                in_hour = 0
                in_minute = 0

    sorted_res = dict(sorted(res.items()))
    answer = []

    for k, time in sorted_res.items():
        tmp = fees[1]
        if time > fees[0]:
            tmp += ((time - fees[0]) // fees[2]) * fees[3]
            if (time - fees[0]) % fees[2] != 0:
                tmp += fees[3]
        answer.append(tmp)
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

