class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for index, value in enumerate(nums):
            mydict[value] = index
        
        for index, value in enumerate(nums):
            complement = target - value

            if complement in mydict and mydict[complement] != index:
                return [index, mydict[complement]]
        return []