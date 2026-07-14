class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in count:
                return [count[target-num], i]
            count[num]=i
        return []