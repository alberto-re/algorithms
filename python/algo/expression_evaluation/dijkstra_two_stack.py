from math import factorial


class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()


class DijkstraTwoStackEvaluator:

    _OPERATORS = ['+', '-', '*', '/', '!']

    def __init__(self):
        self._ops = None
        self._values = None

    def _eval_parenthesis(self):
        operator = self._ops.pop()
        operand = self._values.pop()
        if operator == '+':
            self._values.push(self._values.pop() + operand)
        elif operator == '-':
            self._values.push(self._values.pop() - operand)
        elif operator == '*':
            self._values.push(self._values.pop() * operand)
        elif operator == '/':
            self._values.push(self._values.pop() / operand)
        elif operator == '!':
            self._values.push(factorial(operand))

    def eval(self, expr):
        self._ops = Stack()
        self._values = Stack()

        for token in expr.split():
            if token in self._OPERATORS:
                self._ops.push(token)
            elif token == '(':
                pass
            elif token == ')':
                self._eval_parenthesis()
            else:
                self._values.push(int(token))

        return self._values.pop()


def main():
    expr = input()
    evaluator = DijkstraTwoStackEvaluator()
    print(evaluator.eval(expr))


if __name__ == "__main__":
    main()
