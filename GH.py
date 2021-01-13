#updating in a code
lasss Node:
  def __init__(self,data):
    self.data = data
    self.next = None 
class Linkedlist:
  def __init__(self):
    self.head = None
  def printlist(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next
  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      return
    else:
      last_node = self.head
      while last_node.next:
        last_node = last_node.next
      last_node.next = new_node
  def prepend(self,data):
    new_node = Node(data)
    add_head = self.head
    self.head = new_node
    new_node.next = add_head
  def insert_afr_Node(self,prev_node,data):
    cur_node = self.head
    new_node = Node(data)
    new_node.next = prev_node.next
    while cur_node != prev_node:
      cur_node=cur_node.next
    cur_node.next = new_node
  def delete_node(self,pos):
    cur_node = self.head
    prev_node = None
    count = 0
    if pos == 0:
      self.head = cur_node.next
      cur_node = None
      return
    
    while count < pos:
      prev_node = cur_node
      cur_node = cur_node.next
      count+=1
    prev_node.next = cur_node.next
    cur_node = None
  def length_of_list(self):
    count= 0 
    cur_node = self.head
    while cur_node :
      count = count + 1
      cur_node = cur_node.next
    return count
  def node_swap(self,key1,key2):
    cur_1 = self.head
    prev_1 = None
    while cur_1.data != key1:
      prev_1 = cur_1
      cur_1 = cur_1.next
      
    cur_2= self.head
    prev_2 = None
    while cur_2.data != key2:
      prev_2= cur_2
      cur_2 = cur_2.next
    prev_1.next = cur_2
    prev_2.next = cur_1
    
 
      
    
    
li = Linkedlist()
li.append(7)
li.append(8)
li.append(9)
li.append(10)
li.prepend(6)
li.printlist()
print('-----')
li.node_swap(7,9)
li.printlist()
        
    
    

  
