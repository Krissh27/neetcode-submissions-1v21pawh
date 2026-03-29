class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[]
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        pair.sort()
        fleet=0
        j=len(position)-1
        i=j-1
        while 0<=i:
            if ((target-pair[i][0])/pair[i][1]) <= ((target-pair[j][0])/pair[j][1]):
                i=i-1
            else:
                fleet=fleet+1
                j=i
                i=i-1
        return fleet+1
            


              