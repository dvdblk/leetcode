class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """O(n) time"""
        ranges = []
        # index of the start of the current range
        range_start_i = 0

        for i in range(1, len(nums)):
            # Check if previous number is not consecutive
            if nums[i] - nums[i-1] > 1:
                # check if start of the range is also end of the range
                if i - 1 == range_start_i:
                    ranges.append(str(nums[range_start_i]))
                else:
                    ranges.append(f"{nums[range_start_i]}->{nums[i-1]}")

                range_start_i = i


        # add last number range
        if len(nums) > 1:
            if range_start_i == len(nums)-1:
                ranges.append(str(nums[range_start_i]))
            else:
                ranges.append(f"{nums[range_start_i]}->{nums[len(nums)-1]}")

        return ranges
