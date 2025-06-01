from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            """Helper function to check if a string is valid."""
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:  # Too many closing parentheses
                    return False
            return balance == 0  # Check if all opening parentheses are matched

        # BFS setup
        queue = deque([s])
        visited = set([s])
        found = False
        result = []

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            # If a valid solution has been found, do not process further levels
            if found:
                continue

            # Generate all possible states by removing a single parenthesis
            for i in range(len(current)):
                if current[i] not in "()":
                    continue
                new_string = current[:i] + current[i+1:]
                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result