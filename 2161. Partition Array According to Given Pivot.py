class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        newlist=[]
        cnt=0
        for i in nums:
            if i<pivot:
                newlist.append(i)
            elif i==pivot:
                cnt+=1
        while cnt>0:
            newlist.append(pivot)
            cnt-=1
        for i in nums:
            if i>pivot:
                newlist.append(i)
        return newlist



nums = [9,12,5,10,14,3,10]
pivot = 10
sol = Solution()
print(sol.pivotArray(nums, pivot))