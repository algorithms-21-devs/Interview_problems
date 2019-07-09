import node as n
'''
Time complexity: O(n sqaured)
Algorithm iterates through original list once only. It starts reversing the list,
and then checks in original list if next element is in our reversed in_list.
If it is it means we have a cycle. This check takes n time.
N checks for n elements totaling n squared.
'''

def cycle(node):
    if not node:
        raise Exception('node cannot be of NoneType')

    head = None
    current_node = node

    while current_node:
        #As we reverse the list, if the next node in the original node points
        #to one in our new reversed list then it means there is a cycled
        if in_list(head, node):
            return True
        node = node.next#if not in our list, means no cycle yet so point to next element
        current_node.next = head#the previous node element points to head
        head = current_node#head points to top of list again
        current_node = node#current node now points to top of original list again

    return False


def in_list(node_list, new_node):
    while node_list:#iterate as long as node in list is not None
        if new_node == node_list:#is new_node in our node_list
            return True
        node_list = node_list.next
    return False



#Testing
node_a = n.Node('A')
node_b = n.Node('B')
node_c = n.Node('C')
node_d = n.Node('D')

#'A'->'B'-->'C'->'D'->'B' (cycle)
l1 = node_a
l1.next = node_b
l1.next.next = node_c
l1.next.next.next = node_d
l1.next.next.next.next = node_b #cycle
print(cycle(l1))


node_a = n.Node('A')
node_b = n.Node('B')
node_c = n.Node('C')
node_d = n.Node('D')

#'A'->'B'-->'C'->'D'->'B' (different node with data b)
l2 = node_a
l2.next = node_b
l2.next.next = node_c
l2.next.next.next = node_d
l2.next.next.next.next = n.Node('B') #cycle
print(cycle(l2))

node_a = n.Node('A')
node_b = n.Node('B')
node_c = n.Node('C')
node_d = n.Node('D')

#your_function('A') returns False
l3 = node_a
print(cycle(l3))

node_a = n.Node('A')
node_b = n.Node('B')
node_c = n.Node('C')
node_d = n.Node('D')

#your_function('A'->'B'-->'C') returns False
l4 = node_a
l4.next = node_b
l4.next.next = node_c
print(cycle(l4))

#your_function(none) returns Exception
l5 = None
print(cycle(l5))
