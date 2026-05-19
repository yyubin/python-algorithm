def solution(book_time):
    li = []

    for st, ed in book_time:
        start = to_minutes(st)
        end = to_minutes(ed) + 10
        li.append((start, end))

    li.sort(key=lambda x: (x[0], x[1]))

    first = li.pop(0)
    room = [first[1]]

    for start, end in li:
        min_ = 1e9
        key = -1

        for room_idx, room_end in enumerate(room):
            if room_end <= start and start - room_end < min_:
                min_ = start - room_end
                key = room_idx

        if key == -1:
            room.append(end)
        else:
            room[key] = end

    return len(room)


def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


### 힙으로도 가능

# import heapq
#
# def solution(book_time):
#     times = []
#
#     for st, ed in book_time:
#         start = to_minutes(st)
#         end = to_minutes(ed) + 10
#         times.append((start, end))
#
#     times.sort()
#
#     rooms = []
#
#     for start, end in times:
#         if rooms and rooms[0] <= start:
#             heapq.heappop(rooms)
#
#         heapq.heappush(rooms, end)
#
#     return len(rooms)
#
#
# def to_minutes(time):
#     h, m = map(int, time.split(":"))
#     return h * 60 + m