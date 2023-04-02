import sys

def merge_sort(start, end):
    global cnt
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)

        idx1, idx2 = start, mid + 1
        arr = []

        while idx1 <= mid and idx2 <= end:
            if a[idx1] <= a[idx2]:
                arr.append(a[idx1])
                idx1 += 1
            else:
                arr.append(a[idx2])
                idx2 += 1
                cnt += mid - idx1 + 1

        if idx1 <= mid:
            arr = arr + a[idx1:mid+1]
        if idx2 <= end:
            arr = arr + a[idx2:end+1]

        for i in range(len(arr)):
            a[start+i] = arr[i]

cnt = 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
merge_sort(0, n-1)
print(cnt)
