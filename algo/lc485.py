class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        now = 0
        best = 0
        for x in nums:
            if x == 1:
                now += 1
                if now > best:
                    best = now
            else:
                now = 0
        return best