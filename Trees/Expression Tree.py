class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def is_operator(self, c):
        return c in '+-*/^'

    def build_from_postfix(self, postfix):
        stack = []
        for token in postfix:
            node = Node(token)
            if self.is_operator(token):
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        self.root = stack[-1]

    def inorder(self, node):
        if node:
            if self.is_operator(node.value): print("(", end="")
            self.inorder(node.left)
            print(node.value, end="")
            self.inorder(node.right)
            if self.is_operator(node.value): print(")", end="")

    def preorder(self, node):
        if node:
            print(node.value, end="")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end="")

    def evaluate(self, node):
        if node is None:
            return 0
        if not self.is_operator(node.value):
            return int(node.value)
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        if node.value == '+': return left + right
        if node.value == '-': return left - right
        if node.value == '*': return left * right
        if node.value == '/': return left // right
        if node.value == '^': return left ** right

class ExpressionConverter:
    def __init__(self, expr):
        self.expr = expr.replace(" ", "")

    def precedence(self, op):
        return {'+':1, '-':1, '*':2, '/':2, '^':3}.get(op, 0)

    def infix_to_postfix(self):
        output, stack = [], []
        for ch in self.expr:
            if ch.isalnum():
                output.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(ch) <= self.precedence(stack[-1]):
                    if stack[-1] == '(':
                        break
                    output.append(stack.pop())
                stack.append(ch)
        while stack:
            output.append(stack.pop())
        return output

    def prefix_to_postfix(self):
        stack = []
        for ch in reversed(self.expr):
            if ch.isalnum():
                stack.append(ch)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b + ch)
        return list(stack[0])

def main():
    print("1. Infix Expression")
    print("2. Prefix Expression")
    print("3. Postfix Expression")
    choice = input("Enter expression type (1/2/3): ")

    expr = input("Enter expression: ").replace(" ", "")
    converter = ExpressionConverter(expr)

    if choice == '1':
        postfix = converter.infix_to_postfix()
    elif choice == '2':
        postfix = converter.prefix_to_postfix()
    elif choice == '3':
        postfix = list(expr)
    else:
        print("Invalid choice.")
        return

    tree = ExpressionTree()
    tree.build_from_postfix(postfix)

    print("\n--- Converted Expressions ---")
    print("Postfix :", ''.join(postfix))
    print("Prefix  :", end=" "); tree.preorder(tree.root); print()
    print("Infix   :", end=" "); tree.inorder(tree.root); print()

    print("\n--- Tree Traversals ---")
    print("Inorder   :", end=" "); tree.inorder(tree.root); print()
    print("Preorder  :", end=" "); tree.preorder(tree.root); print()
    print("Postorder :", end=" "); tree.postorder(tree.root); print()

    if all(c.isdigit() or c in '+-*/^()' for c in expr):
        result = tree.evaluate(tree.root)
        print("\nEvaluated Result:", result)
    else:
        print("\nContains variables — skipping evaluation.")

if __name__ == "__main__":
    main()
