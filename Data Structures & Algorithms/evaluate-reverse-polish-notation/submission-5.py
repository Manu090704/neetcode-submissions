class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for c in tokens:
            if c == "+":
                firstElement = numbers.pop()
                secondElement = numbers.pop()
                add = firstElement + secondElement
                numbers.append(add)
            elif c == "-":
                firstElement = numbers.pop()
                secondElement = numbers.pop()
                rest = secondElement - firstElement
                numbers.append(rest)
            elif c == "*":
                firstElement = numbers.pop()
                secondElement = numbers.pop()
                multiply = firstElement * secondElement
                numbers.append(multiply)
            elif c == "/":
                firstElement = numbers.pop()
                secondElement = numbers.pop()
                division = int(float(secondElement)/firstElement)
                numbers.append(division)
            else:
                numbers.append(int(c))
            
        return numbers[0]