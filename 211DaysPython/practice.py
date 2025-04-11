
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], idx]

        seen[num] = idx
print(twoSum([2,7,11,15], 9))