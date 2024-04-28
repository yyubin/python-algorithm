for i in range(10):
    cnt = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(cnt):
        max_idx, min_idx = boxes.index(max(boxes)), boxes.index(min(boxes))
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    print('#'+str(i+1), max(boxes) - min(boxes))
