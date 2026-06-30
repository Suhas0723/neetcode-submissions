
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])

        while len(queue1) > 0 and len(queue2) > 0:
            curr1 = queue1.popleft()
            curr2 = queue2.popleft()
            
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False

            queue1.append(curr1.left)
            queue1.append(curr1.right)
            queue2.append(curr2.left)
            queue2.append(curr2.right)
        
        return True


