# 1822. Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num == 0:
                return 0
            res *= num // abs(num)
        return res
