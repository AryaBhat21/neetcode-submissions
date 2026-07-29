class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        for i in s1:
            count1[i] = count1.get(i,0)+1
        for i in s2:
            count2[i] = count2.get(i,0)+1

        for i in count1:
            if count1[i]!=count2[i]:
                return False
        
        return True