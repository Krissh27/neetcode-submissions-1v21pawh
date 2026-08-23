class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time=0
        ans=0

        for i in customers:
            if time>i[0]:
                ans+=time-i[0]
            else:
                time=i[0]
            ans+=i[1]
            time+=i[1]
        return ans/len(customers)
            
            
