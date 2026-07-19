class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        buckets = []
        for x in freq:
            buckets.append(freq[x])

        buckets=sorted(buckets)
        buckets=buckets[-k:]
        ans=[]
        for x in freq:
            if freq[x] in buckets:
                ans.append(x)

        return ans
