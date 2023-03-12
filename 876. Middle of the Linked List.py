###Python


## 将链表里的数据提出来放到list中，然后直接提取。Take the data out of the linked list and put it to the list.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/middle-of-the-linked-list/solution/lian-biao-de-zhong-jian-jie-dian-by-leetcode-solut/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
