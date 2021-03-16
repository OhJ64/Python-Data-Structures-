#return the indexs of list/array that add up to the target value
def twoSum(self, nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return None
