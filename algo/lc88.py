class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """nums1[:] = sorted(nums1[:m] + nums2) в лоб, сложность O((m + n) * log (m + n)), память O(m + n)"""
        a1 = m
        a2 = n
        t = m + n - 1
        while a2 > 0:
            if a1 > 0 and nums1[a1 - 1] >= nums2[a2 - 1]:
                nums1[t] = nums1[a1 - 1]
                a1 -= 1
            else:
                nums1[t] = nums2[a2 - 1]
                a2 -= 1
            t -= 1
        """это решение на сложность O(n+m) и константа памяти O(1)"""