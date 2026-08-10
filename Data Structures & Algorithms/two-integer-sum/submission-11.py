class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for index, value in enumerate(nums):
            if value not in mydict:
                mydict[value] = index
        #created the dictionary
        for index, value in enumerate(nums):
            complement = target - value
            if complement in mydict and mydict[complement] != index:
                return sorted([index, mydict[complement]])
        return []