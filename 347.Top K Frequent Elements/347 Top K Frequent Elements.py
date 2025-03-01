class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Frequency_Dictionary=dict()
        final_list1=[]
        final_list=[]
        y=0
        for i in nums:
            if i in Frequency_Dictionary:
                Frequency_Dictionary[i] += 1
            else:
                Frequency_Dictionary[i] = 1
        
        for i in Frequency_Dictionary:
            final_list.append(i)
        final_list = sorted(final_list, reverse=True)

        while y<k :
            final_list1.append(final_list[y])
            y=y+1
        return final_list1
            
# My Approach
# Goal: Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Example:
# Input = [1,1,1,2,2,3], k = 2
# Output = [1,2]

# We need to count all the elements we have.
# To do that, we can use a frequency array.

# A frequency array is basically an array where each index maps to the number of times that element is repeated in the list.
# For example, a frequency array for [1,1,1,2,2,3] would look like this: [0,3,2,1]
# The first index is 0, and its value is 0 because the element 0 doesn't appear in our list.
# The second index is 1, and its value is 3 because the element 1 appears three times in the list, etc.

# Now you can see that the length of our frequency array depends on the largest element in our input list.
# For example, if our element list is [9,10], our frequency array will be:
# [0,0,0,0,0,0,0,0,0,1,1]
# This is very memory inefficient.

# Instead, we can use a DICTIONARY(Hashmap).
# A dictionary is like an array, but you can choose any index you want, and it doesn't have to be sequential.
# For example, a frequency dictionary for the array mentioned above would look like this:
# {
#     9: 1,
#     10: 1
# }
# This means that there is an index 9 with a value of 1 and an index 10 with a value of 1.
# Using a dictionary allows us to store only the necessary elements without wasting memory on unused indices.
