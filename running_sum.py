def runningSum(nums: list[int]) -> list[int]:
    total = 0
    return [total := n + total for n in nums]


print(runningSum([1, 2, 3, 4]))
