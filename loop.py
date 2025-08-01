# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Root adalah elemen pertama preorder
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Temukan indeks root di inorder
        idx = inorder.index(root_val)
        
        # Bagi preorder dan inorder untuk subtree kiri dan kanan
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        
        return root
