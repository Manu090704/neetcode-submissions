class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            rest = target - n
            if rest in hashMap:
                return [hashMap[rest],i]
            hashMap[n] = i
        return []