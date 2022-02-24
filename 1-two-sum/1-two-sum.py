class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dp = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dp:
                return [i, dp[diff]]
            dp[num] = i
            