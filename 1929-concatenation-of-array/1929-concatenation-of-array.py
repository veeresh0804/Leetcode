class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[]
        for ch in nums:
            res.append(ch)
        for ch in nums:
            res.append(ch)
        return res