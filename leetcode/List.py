class ListNode:
    def __init__(self) -> None:
        self.val = None
        self.next = None

#  建立一个单列表

out = ListNode()
out.val = 0
curr = out


for i in range(3):
    next = ListNode()
    next.val = i + 1
    
    curr.next = next 
    curr = next 
    


def traverse(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next




# 反转列表

def reverseList(head):
    
    # prev, curr, next

    # init 
    prev = None
    curr = head

    while curr:
        # print(curr.val)

        # 存在下一个节点    
        next = curr.next
        
        # 核心操作
        curr.next = prev

        # 移动指针
        prev = curr
        curr = next

    return prev


# traverse(out)

traverse(reverseList(out))


