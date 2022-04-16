class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        opnums=[]
        for i in range(len(nums)//2):
            opnums.append(nums[i])
            opnums.append(nums[i+n])
        return opnums