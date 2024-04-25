numbers = input().split()


def reverse(idx, nums):
    if idx == len(nums) // 2:
        return

    swap_idx = len(nums) - 1 - idx
    nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
    reverse(idx + 1, nums)


reverse(0, numbers)
print(' '.join(numbers))
