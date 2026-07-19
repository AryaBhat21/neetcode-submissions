class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append("akshi")
        return "\t".join(strs)

    def decode(self, s: str) -> List[str]:
        
        res = s.split("\t")
        res.pop()
        return res