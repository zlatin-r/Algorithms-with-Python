numbers = [int(x) for x in input().split()]
target = int(input())


def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid

        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1
