class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1={}
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
            if len(dict1)>2:
                newd={}
                
                for j in dict1:
                    if dict1[j]>1:
                        newd[j]=dict1[j]-1
                dict1=newd

                
            
        list1=[]
        for i in dict1:
            if nums.count(i)>len(nums)/3:
                list1.append(i)
        return list1

        
