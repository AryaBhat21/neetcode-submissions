class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append("akshi")
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        
        res = s.split("\n")
        res.pop()
        return res