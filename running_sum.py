def runningSum(nums: list[int]) -> list[int]:
    sum = 0
    res = []
    for n in nums:
        sum += n
        res.append(sum)
    return res


print(runningSum([1, 2, 3, 4]))
