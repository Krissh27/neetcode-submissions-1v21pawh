class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack1 = []
        for i in operations:
            if i == "+":
                stack1.append(stack1[-1] + stack1[-2])
            elif i == "D":
                stack1.append(2 * stack1[-1])
            elif i == "C":
                stack1.pop()
            else:
                stack1.append(int(i))
        return sum(stack1)