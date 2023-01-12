class Solution:
    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left:
            return not right
        if not right:
            return False
        return left.val == right.val

    def traverse(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not self.check(left, right):
            return False

        if left and right:
            return self.traverse(left.left, right.right) and self.traverse(
                left.right, right.left
            )

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root.left, root.right)
