class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        num_list = [(n,i) for i,n in enumerate(nums)]
        num_list.sort()
        
        i = 0
        j = len(nums) - 1
        while i < j:
            total = num_list[i][0] + num_list[j][0]
            if total == target:
                return [num_list[i][1],num_list[j][1]]
            elif total > target:
                j -= 1
            else:
                i += 1
        return []