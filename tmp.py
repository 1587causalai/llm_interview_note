# 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，同时满足 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 1. 暴力法
# 思路是直接遍历所有的三元组，找出和为 0 的三元组，然后去重。
def threeSum(nums):
    n = len(nums)
    nums.sort()
    ans = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.add((nums[i], nums[j], nums[k]))
    return list(ans)

# test code
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) # [[-1, -1, 2], [-1, 0, 1]]


# 2. 双指针法
# 思路是先将数组排序，然后遍历排序后的数组，对于每个元素，用双指针法找出和为 0 的两个元素。
def threeSum(nums):
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return res

# test code
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) # [[-1, -1, 2], [-1, 0, 1]]


# filename: 06_three_sum.py


