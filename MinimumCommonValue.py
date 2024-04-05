class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        common = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        
        return -1
            

solution = Solution()
nums1 = [1,1,2]
nums2 = [2,4]
print(solution.getCommon(nums1, nums2))
