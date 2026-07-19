class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
            
        seen = set()
        stack = []
        
        for c in s:
            count[c] -= 1
            if c in seen:
                continue
                
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                seen.remove(stack.pop())
                
            stack.append(c)
            seen.add(c)
            
        return "".join(stack)