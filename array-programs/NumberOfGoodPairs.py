"""
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Input: nums = [1,2,3]
Output: 0   
"""

nums = [1,2,3]
count = list(range(0,100))
totalcount = 0
for i in nums:
    # print(count[i])
    totalcount = count[i]+1
    print(count[i]+1, "count[i]+1")

print(f" totalcount {totalcount}")
# count = 0
# output_list = []
# for i in range(len(nums)):
#     print(f" i : {i}")
#     for j in range(i):
#         print(f" j : {j}")
#         if nums[i] == nums[j]:
#             output_list.append(nums[i])
#             # print(nums[i], nums[j])

# print(output_list)
# # return len(output_list)

