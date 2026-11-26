class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        srt = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                srt[i] = nums[right] ** 2
                right -= 1
            else:
                srt[i] = nums[left] ** 2
                left += 1
        return srt