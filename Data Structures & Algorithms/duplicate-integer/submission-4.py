class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1

        for i in d:
            if d[i]>1:
                return True
        
        return False