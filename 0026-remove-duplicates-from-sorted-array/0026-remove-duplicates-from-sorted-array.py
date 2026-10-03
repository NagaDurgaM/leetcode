class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # k tracks the position for the next unique element
        k = 1

        for i in range(1, len(nums)):
            # When a new unique element is found
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
