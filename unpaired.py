#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):  # Add 'self' as the first parameter
        # Use a set to keep track of unique elements
        unique = set()

        # Iterate through the array
        for num in nums:
            # If the element is already in the set, it's a duplicate, return True
            if num in unique:
                return True
            else:
                # Otherwise, add it to the set
                unique.add(num)

        # If the loop completes without finding duplicates, return False
        return False

# Example usage:
nums1 = [1, 2, 3, 4, 5]
print(Solution().containsDuplicate(nums1))  # Output: False

nums2 = [1, 2, 3, 4, 1]
print(Solution().containsDuplicate(nums2))  # Output: True

 