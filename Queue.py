#This queue adds new items at the tail of a list and removes items at the head. 

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value)) 

    __repr__ = __str__


class Queue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if self.head== None:
            return True
        else:
            return False
   
    def size(self):
        count= 0
        temp= self.head
        while temp!= None:
            count+=1
            temp= temp.next
        return count

    def enqueue(self, item):
        new_node= Node(item)
        if self.head== None:
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.next= new_node
            self.tail= new_node

    def dequeue (self):
        if self.head== None:
            return "Queue is empty"
        else:
            val= self.head.value
            self.head= self.head.next
            return val
    

      
    def printQueue(self):
        temp = self.head
        while (temp):
            print(temp.value, end=' ')  
            temp = temp.next

            