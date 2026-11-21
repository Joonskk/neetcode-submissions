class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zer_cnt = 1, 0
        n = len(nums)
        res = [0] * n

        for num in nums:
            if num:
                prod *= num
            else:
                zer_cnt += 1
        if zer_cnt > 1:
            return res

        for i, c in enumerate(nums):
            if zer_cnt:
                if c == 0:
                    res[i] = prod
            else:
                res[i] = prod // c

        return res