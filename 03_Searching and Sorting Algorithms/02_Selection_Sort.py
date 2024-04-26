numbers = [int(x) for x in input().split()]

for idx in range(len(numbers)):
    min_idx = idx
    for curr_idx in range(idx + 1, len(numbers)):
        if numbers[curr_idx] < numbers[min_idx]:
            min_idx = curr_idx
    numbers[min_idx], numbers[idx] = numbers[idx], numbers[min_idx]

print(*numbers, sep=" ")
