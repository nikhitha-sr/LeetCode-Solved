class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp={}
        for index in range(len(nums)):
            rem = target - nums[index]
            if rem in tmp:
                return ([index,tmp[rem]])
            else:
                tmp[nums[index]] = index
        return []         
        