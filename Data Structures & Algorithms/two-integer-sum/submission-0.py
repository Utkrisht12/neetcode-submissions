class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        diff=0
        set1={}
        ans=[]
        for x,y in enumerate(nums):
            diff=target-y
            if diff in set1:
                ans.append(set1[diff])
                ans.append(x)
                return ans
            set1[y]=x
        return ans
