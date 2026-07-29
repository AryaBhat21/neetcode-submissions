class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            for i in seen:
                return True
            seen.add(i)
            return False
                          
