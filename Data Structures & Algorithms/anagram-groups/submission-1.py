class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check(s,t):
            if len(s)!=len(t):
                return False
                
            d = {}
            for char in s:
                d[char] = d.get(char,0)+1
            
            for char in t:
                if char in d:
                    d[char]-=1
            
            for val in d.values():
                if val != 0 :
                    return False
            
            return True

        ans=[]
        visited = [False] * len(strs)
        
        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True
            
            for j in range(i + 1, len(strs)):
                if not visited[j] and check(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            ans.append(group)
            
        return ans