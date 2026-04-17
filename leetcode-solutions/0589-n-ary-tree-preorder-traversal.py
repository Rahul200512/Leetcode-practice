class Solution:
    # binary search on sorted array
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Add children in reverse order so the first child is processed first
            if node.children:
                for child in reversed(node.children):
                    stack.append(child)

        return result
