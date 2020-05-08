"""
150. Evaluate Reverse Polish Notation
Medium: Stack

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
class Solution:
    def evalRPN(self, tokens):
        symbols = set(["/", "*", "+", "-"])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in symbols:
                stack.append(int(tokens[i]))
            if tokens[i] in symbols:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if tokens[i] == "/":
                    """
                    Be careful with the if function below
                    in Python, it returns -1, while in 
                    Leetcode it should return 0
                    """
                    if temp1*temp2 < 0 and temp2 % temp1 != 0: 
                        temp3 = temp2 // temp1 + 1
                    else:
                        temp3 = temp2 // temp1
                if tokens[i] == "*":
                    temp3 = temp1 * temp2
                if tokens[i] == "+":
                    temp3 = temp1 + temp2
                if tokens[i] == "-":
                    temp3 = temp2 - temp1  
                stack.append(temp3)
            # print(stack)
        return stack.pop()

tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["4","-2","/","2","-3","-","-"]
s = Solution()
print(s.evalRPN(tokens))











