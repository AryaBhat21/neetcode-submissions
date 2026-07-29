class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append("akshi")
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        
        res = s.split(" ")
        res.pop()
        return res