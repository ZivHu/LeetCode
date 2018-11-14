# -*- coding: utf-8 -*-
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""
from collections import Counter

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 解法一
        # k = []
        # result = []
        # for i, a in enumerate(nums):
        #     for j, b in enumerate(nums[i+1::]):
        #         for _, c in enumerate(nums[j+1::]):
        #             if a + b + c == 0 and Counter([a, b, c]) not in k:
        #                 k.append(Counter([a, b, c]))
        # for i in k:
        #     result.append(list(i.elements()))
        # return result

        # 解法二
        num_hush = {}
        result = list()
        for num in nums:
            num_hush[num] = num_hush.get(num, 0) +1
        if 0 in nums and num_hush[0] >= 3:
            result.append([0, 0, 0])
        nums = sorted(list(num_hush.keys()))
        for i, num in enumerate(nums):
            for j in nums[i+1:]:
                if num*2 + j == 0 and num_hush[num] >= 2:
                    result.append([num, num, j])
                if j*2 + num == 0 and num_hush[j] >= 2:
                    result.append([num, j, j])
                dif = 0 - num - j
                if dif > j and dif in num_hush:
                    result.append([num, j, dif])
        return result


a = Solution()
print(a.threeSum([1,-1,1,2,-2,0]))
