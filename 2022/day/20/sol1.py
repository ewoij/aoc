vals = list(map(int, open('2022/day/20/input')))

class Node:
    val: int
    next = None
    prev = None

    def __init__(self, val):
        self.val = val


nodes = [Node(v) for v in vals]

for i in range(0, len(nodes)-1):
    nodes[i].next = nodes[i+1]
nodes[-1].next = nodes[0]

for i in range(1, len(nodes)):
    nodes[i].prev = nodes[i-1]
nodes[0].prev = nodes[-1]

head = nodes[0]

def print_list(curr, len_):
    r = []
    for _ in range(len_):
        r.append(curr.val)
        curr = curr.next
    print(r)


for node in nodes:
    if node == head:
        head = node.next

    # remove the node
    node.prev.next = node.next
    node.next.prev = node.prev

    curr = node.prev
    if node.val < 0:
        for _ in range(-node.val):
            curr = curr.prev
    else:
        for _ in range(node.val):
            curr = curr.next

    # insert after
    node.prev = curr
    node.next = curr.next
    node.prev.next = node
    node.next.prev = node


# find 0
curr = head
while True:
    if curr.val == 0:
        break
    curr = curr.next

for i in range(1000):
    curr = curr.next

_1 = curr.val

for i in range(1000):
    curr = curr.next

_2 = curr.val

for i in range(1000):
    curr = curr.next

_3 = curr.val

print(_1, _2, _3, _1 + _2 + _3)
