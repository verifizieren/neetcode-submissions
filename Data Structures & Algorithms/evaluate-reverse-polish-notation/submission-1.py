class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok = tokens.pop()

        if tok in {"+", "-", "*", "/"}:
            right = self.evalRPN(tokens)
            left = self.evalRPN(tokens)

            if tok == "+":
                return left + right
            if tok == "-":
                return left - right
            if tok == "*":
                return left * right
            return int(left / right)

        return int(tok)