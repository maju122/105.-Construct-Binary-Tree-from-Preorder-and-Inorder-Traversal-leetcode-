class Solution(object):
    def buildTree(self, preorder, inorder):
        index_of = {}
        for i, val in enumerate(inorder):
            index_of[val] = i

        self.pre_idx = 0

        def build(lo, hi):
            if lo > hi:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = index_of[root_val]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)
