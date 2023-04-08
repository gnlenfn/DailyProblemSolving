class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        numbers = []
        for idx, n in enumerate(nums):
            numbers.append((n, idx))
        numbers.sort()
        while left < right:
            sums = numbers[left][0] + numbers[right][0]
            if sums == target:
                return [numbers[left][1], numbers[right][1]]
            
            elif sums < target:
                left += 1
            
            elif sums > target:
                right -= 1