###Python

##My solutions

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            result.append(sum(nums[:i+1]))
        return result
      
##Maybe better solution:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
         for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
         return nums
      
