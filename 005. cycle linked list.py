# created via gpt
#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# generate a chain
def createLinkedList(nums, pos):
    if not nums:
        return None

    nodes = [ListNode(num) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

# test
head_values = [3, 2, 0, -4]
pos = 1
head = createLinkedList(head_values, pos)
result = hasCycle(head)
print(result)


# In[ ]:




