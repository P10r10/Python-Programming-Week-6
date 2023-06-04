def maximumWealth(accounts: list[list[int]]) -> int:
    return max([sum(n) for n in accounts])

print(maximumWealth([[1,5],[7,3],[3,5]]))