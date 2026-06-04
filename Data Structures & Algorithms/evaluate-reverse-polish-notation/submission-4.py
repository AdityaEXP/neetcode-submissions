class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                second = number_stack.pop()
                first = number_stack.pop()

                number_stack.append(
                    int(eval(f"{first}{token}{second}"))
                )
                continue
            
            number_stack.append(int(token))

        print(number_stack[-1])
        return number_stack[-1]


