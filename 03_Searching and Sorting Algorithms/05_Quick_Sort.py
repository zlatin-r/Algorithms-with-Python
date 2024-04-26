def quick_sort(start, end, nums):
    if start >= end:
        return

    pivot, left, right = start, start + 1, end

    while left <= right:

        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quick_sort(start, right - 1, nums)
    quick_sort(right + 1, end, nums)


numbers = [int(x) for x in input().split()]
quick_sort(0, len(numbers) - 1, numbers)

print(*numbers, sep=' ')
