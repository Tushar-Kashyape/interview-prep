def coin(nums):
    if len(nums) <= 1: return nums[0]

    l, r = 0, len(nums)-1
    while l < r:
        if nums[r] > nums[l]: r -= 1
        else: l += 1

    if l == r:
        return nums[l]
    else:
        return min(nums[l], nums[r])

arr = [5, 3, 1, 6, 9]
print(coin(arr))