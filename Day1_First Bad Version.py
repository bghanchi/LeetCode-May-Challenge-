#Problem Link:-https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

#Solution:-

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        low=1
        high=n
        mid=0
        first=0
        while low<=high:
            mid=low+int((high-low)/2)
            if isBadVersion(mid):
                first=mid
                high=mid-1                
            else:
                low=mid+1
        return first        
        """
        :type n: int
        :rtype: int
        """
        
#Approach:- Simple use binary search  
#Time Complexity:- O(logn)       