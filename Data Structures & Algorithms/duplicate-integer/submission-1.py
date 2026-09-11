class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for num in nums:
            if(num in array):
                return True
            else:
                array.append(num)
                
        return False
        

        