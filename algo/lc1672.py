def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = []
        for row in accounts:
            wealth.append(sum(row))
        return max(wealth)