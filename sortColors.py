class Solution:
    def sortColors(self, nums: list[int]):
        def selection_sort(arr):
            for i in range(0, len(arr) - 1):
                min_idx = i
                for j in range(i + 1, len(arr)):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
            return arr
        
        sortedColors = selection_sort(nums)
        return sortedColors
