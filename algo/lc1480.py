# LC 1480. Running Sum of 1d Array
# Идея: копим текущую сумму в одной переменной
# Время: O(n)  Память: O(1)

def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        total_sum = 0
        for i in nums:
            total_sum += i
            ans.append(total_sum)
        return ans