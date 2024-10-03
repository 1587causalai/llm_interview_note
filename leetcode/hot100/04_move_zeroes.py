# 移动零

## 1. 暴力解法

def moveZeroes(nums):
    zeros = [x for x in nums if x == 0]
    non_zeros = [x for x in nums if x != 0]
    return non_zeros + zeros

# test code
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

## 2. 双指针法
def moveZeroes(nums):
    n = len(nums)
    left = 0
    right = 0
    while right < n:
        # 当右指针指向的元素不为0时，交换左右指针指向的元素
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            # 请注意, left 指针是移动的
            left += 1
        right += 1

# test code
nums = [0, 0, 1, 3, 12]
moveZeroes(nums)
print(nums)