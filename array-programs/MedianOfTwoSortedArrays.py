"""
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
nums1 = [1,2]
nums2 = [2,3]
sorted_array = sorted(nums1 + nums2)
if len(sorted_array) % 2 == 0:
    index1 = int(len(sorted_array) / 2)
    index2 = index1 + 1
    print(index1)
    print(index2)
    mid = (sorted_array[index1] + sorted_array[index2]) / 2

else:
    index = (len(sorted_array) / 2)
    print(index)
    indx = index + 0.5
    mid = sorted_array[int(indx)]

print(mid)


