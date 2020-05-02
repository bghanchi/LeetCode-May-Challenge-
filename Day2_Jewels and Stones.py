#Problem Link:-https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

#Solution:-

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Hashmap=dict()
        for i in J:
            Hashmap[i]=1
        count=0
        for i in S:
            if Hashmap.get(i)!=None:
                count+=1
        return count        
                
#Approach:- Hashmap  
#Time Complexity:- O(max(len(j),len(S)))       