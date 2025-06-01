class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        sequence = [0] * (2 * n - 1)  # Initialize the sequence with zeros
        used = [False] * (n + 1)  # Track whether each number is used

        def backtrack(index):
            # If the sequence is fully filled, return True
            if index == len(sequence):
                return True

            # If the current position is already filled, move to the next index
            if sequence[index] != 0:
                return backtrack(index + 1)

            # Try placing numbers from n to 1 (lexicographically largest first)
            for num in range(n, 0, -1):
                if used[num]:
                    continue  # Skip if the number is already used

                if num == 1:  # Special case for 1 (only one occurrence)
                    sequence[index] = 1
                    used[1] = True

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    sequence[index] = 0
                    used[1] = False
                else:
                    # Check if `num` can be placed at `index` and `index + num`
                    if index + num < len(sequence) and sequence[index + num] == 0:
                        sequence[index] = num
                        sequence[index + num] = num
                        used[num] = True

                        if backtrack(index + 1):
                            return True

                        # Backtrack
                        sequence[index] = 0
                        sequence[index + num] = 0
                        used[num] = False

            return False

        backtrack(0)  # Start backtracking from index 0
        return sequence