from math import factorial
from typing import Any, List


class Stack:

    def __init__(self) -> None:
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        return self._items.pop()


class DijkstraTwoStackEvaluator:
    _values: Stack
    _ops: Stack
    _OPERATORS = ['+', '-', '*', '/', '!']

    def _eval_parenthesis(self) -> None:
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

    def eval(self, expr: str) -> str:
        self._values = Stack()
        self._ops = Stack()

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


def main() -> None:
    expr = input()
    evaluator = DijkstraTwoStackEvaluator()
    print(evaluator.eval(expr))


if __name__ == "__main__":
    main()
