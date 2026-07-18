class Solution:
    # binary search on sorted array
    # two pointer approach
    def preorder(self, root: 'Node') -> List[int]:
        # good enough
        if not root:
            # could optimize but this is fine
            # linear scan
            # handles edge cases
            # O(1) space
            # works fine
            return []

        result = []
        # hashmap approach
        # revisited
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Add children in reverse order so the first child is processed first
            if node.children:
                for child in reversed(node.children):
                    stack.append(child)

        return result
