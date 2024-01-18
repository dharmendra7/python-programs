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
frequency = {}
count = 0

for num in nums:
    if num in frequency:
        count += frequency[num]    
        frequency[num] += 1
    else:
        frequency[num] = 1
        
print(frequency)

print(count)     
