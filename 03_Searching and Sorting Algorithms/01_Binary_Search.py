def binary_search(nums, trg):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == trg:
            return mid

        if nums[mid] < trg:
            left = mid + 1
        else:
            right = mid - 1
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target))
