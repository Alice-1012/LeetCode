# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(max(nums))
        
        def makeTree(nums,root):
            left = nums[:nums.index(root.val)] #root값-1번째 까지 left 배열로 가져감
            right = nums[nums.index(root.val)+1:] #root값+1번째 부터 right 배열로 가져감
            
            if not nums: #nums에 값이 없으면 종료
                return
            
            if len(left) > 0:
                root.left = TreeNode(max(left))#root의 왼쪽에 left배열의 max값을 지정
                makeTree(left, root.left)#makeTree 메소드에 left배열과 root.left(새로운 root)값 넘겨줌
            
            if len(right) > 0:
                root.right = TreeNode(max(right))
                makeTree(right, root.right)
                
        makeTree(nums,root)
        return root