class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None


my_linked_list = Doubly_Linked_List()
    

def linkedlist_traversal(head_node):
    count = 0
    temporary_node = head_node
    while temporary_node != None:
        print(temporary_node.data, end = "->")
        previous_node = temporary_node.prev
        temporary_node = temporary_node.next
        #previous_node = temporary_node.prev
        count += 1
    print("\n Number of elements in the linked list is : ", count)
    print("Print data in reverse direction...")
    previous_node = previous_node.next
    while previous_node != None:
        print(previous_node.data, end = "->")
        previous_node = previous_node.prev
    

def linkedlist_search(head_node, element):
    temporary_node = head_node
    flag = False
    while temporary_node != None:
        if temporary_node.data == element:
            flag = True
            print("Element found")
            break
        temporary_node = temporary_node.next
    if flag == False:
        print("Element not found")
            



# Create a Doubly linked list with 10 nodes for demo purpose
node_elements = [15,14,13,12,11,16,17,18,19,10]

for i in range(10):
    new_node = Node(node_elements[i])
    if my_linked_list.head==None:  # Inserting first element
        my_linked_list.head = new_node
    else:
        temporary_node = my_linked_list.head
        while temporary_node.next != None:
            temporary_node = temporary_node.next
        temporary_node.next = new_node
        new_node.prev = temporary_node

linkedlist_traversal(my_linked_list.head)

