class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            level_order[level].append(node.val)   # no check needed
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        # convert to list of lists
        return [level_order[i] for i in sorted(level_order)]    