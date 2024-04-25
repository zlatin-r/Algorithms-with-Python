def loop_gen(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for i in range(1, len(arr) + 1):
        arr[idx] = i
        loop_gen(idx + 1, arr)


n = int(input())
arr = [None] * n

loop_gen(0, arr)
