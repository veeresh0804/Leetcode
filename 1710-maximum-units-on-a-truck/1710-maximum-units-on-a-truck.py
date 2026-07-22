class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def get_units(box):
            return box[1]
            
        boxTypes.sort(key=get_units, reverse=True)
        
        ans = 0
        for count, units in boxTypes:
            if truckSize == 0:
                break
            
            take = min(count, truckSize)
            ans += take * units
            truckSize -= take
            
        return ans