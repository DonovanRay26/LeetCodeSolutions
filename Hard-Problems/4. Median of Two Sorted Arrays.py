# import statements: don't need to add these to solutions
from math import floor

"""
This is the solution I used to solve Problem 4. Median of Two Sorted Arrays.

My first problem solving steps were:
    1. Read problem description and understand requirements, use of inputs, and expected outputs
    2. Create a general approach to the problem
    3. Develop algorithm
    
My algorithm is as follows:
    1. Create an empty array to merge the values from nums1 and nums2 into
    2. Merge nums1 and nums2 into the merged array
    3. Sort the merged array using built-in sort method, .sort()
    4. Determine if the length of the array is odd or even, then:
        4.a If odd, return the middle value of the array (this will be the median as it has been sorted numerically)
        4.b If even, return the average of the two middle values of the array (again, will be the median due to sorting)
        
        note: using math.floor for this is very helpful, however you can just use floor()
        
This solution (as of the time of submission) beats 99.98% of other solutions, using 38ms of runtime with a time 
complexity of O(Nlog(N)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # merge arrays and sort:
        merged = []
        for num in nums1:
            merged.append(num)
        for num in nums2:
            merged.append(num)
        merged.sort()

        # get median:
        length = len(merged)

        # if odd amount, return just the middle number:
        if length % 2 > 0:
            return merged[int(floor(length / 2))]

        # if even amount, return the average of the two middle numbers:
        else:
            return (float(merged[(length / 2) - 1]) + float(merged[length / 2])) / 2