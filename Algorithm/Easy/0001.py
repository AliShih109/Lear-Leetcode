'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution():
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        
        my_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in my_dict: #用dict就只需掃1次而不是2次
                return [my_dict[target - nums[i]], i]
            else:
                my_dict[nums[i]] = i
