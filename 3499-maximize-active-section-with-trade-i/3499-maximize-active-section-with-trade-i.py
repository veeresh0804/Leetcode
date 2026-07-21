class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        aug = '1' + s + '1'
        
        zero_blocks = []
        curr_zeros = 0
        
        for ch in aug:
            if ch == '0':
                curr_zeros += 1
            else:
                if curr_zeros > 0:
                    zero_blocks.append(curr_zeros)
                    curr_zeros = 0
                    
        if len(zero_blocks) < 2:
            return initial_ones
            
        max_zeros = 0
        for i in range(len(zero_blocks) - 1):
            max_zeros = max(max_zeros, zero_blocks[i] + zero_blocks[i + 1])
            
        return initial_ones + max_zeros