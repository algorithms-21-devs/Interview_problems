import node as n
'''
Time complexity: O(n)
Algorithm iterates through link list once only. It adds memory location as a key to a dictionary. As it iterates it checks if the
current node memory matches any in the dictionary in O(1) time. If it does a cycle must be present.
'''

def cycle(head_node):
    #must be a linked list
    if head_node is None:
        raise Exception('Cannot process an empty linked list')

    current_node = head_node
    nodes_dic = {}#stores memory locations as keys and data of node as value

    #iterate through the list once
    while current_node is not None:
        if current_node not in nodes_dic:#put in dictionary if node is not in dic
            nodes_dic[current_node] = current_node.data
        else:#we found a node twice meaning there is a cycle
            return True

        current_node = current_node.next#make sure we iterate through the list
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



#'A'->'B'-->'C'->'D'->'B' (different node with data b)
l2 = node_a
l2.next = node_b
l2.next.next = node_c
l2.next.next.next = node_d
l2.next.next.next.next = n.Node('B') #cycle
print(cycle(l2))

#your_function('A') returns False
l3 = node_a
print(cycle(l3))


#your_function('A'->'B'-->'C') returns False
l4 = node_a
l4.next = node_b
l4.next.next = node_c
print(cycle(l4))

#your_function(none) returns Exception
l5 = None
print(cycle(l5))
