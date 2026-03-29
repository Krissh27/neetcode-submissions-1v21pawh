class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result =[]
        for i in asteroids:
            status=False
            
            while result and (i<0 and result[-1] > 0):
                if abs(result[-1])>abs(i):
                    status=True
                    break
                elif abs(result[-1])<abs(i):
                    result.pop()
                    
                else:
                    result.pop()
                    status=True
                    
                    break
            if status==False:
                result.append(i)


                
        return result


                


                

            
        
            




        