# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
    
    def __str__(self):
        '''for testing purposes'''
        p = self.head
        st = ''
        while (p != None):
            st = st + ' ' + str(p.data)
            p = p.next
        return st
        
    def add(self, value):
        '''Add a node with the value parameter as data to the tail of the list'''
        if self.head == None:
            self.head = Node(value)
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = Node(value)

    def delete(self, value):
        '''delete the node with the value parameter from the appropriate position in the list and link the surrounding nodes'''
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next
            temp = None
        else:
            p = self.head
            t = self.head.next
            while  t.data != value and t.next != None:
                p = p.next
                t = t.next
            p.next = t.next
            t = None
            
    def reverseNonResursive(self):
        prevptr = None;
        while self.head != None:
            nextptr = self.head.next;
            self.head.next = prevptr
            prevptr = self.head
            self.head = nextptr
        self.head = prevptr
        return self


    def reverseRecursive(self):
        self.head = self.reverseRecursiveHelper(self.head, None)
        return self

    def reverseRecursiveHelper(self, head, prev):
        if head == None:
            return head
        #elif prev != None:
        
        nextptr = head.next
        head.next = prev

        return self.reverseRecursiveHelper(nextptr, head)



    


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
        
    
        
        
        
        




linkedlist = LinkedList()
linkedlist.add(5)
linkedlist.add(3)
linkedlist.add(10)
linkedlist.add(15)

print(linkedlist.reverseRecursive())
#print(linkedlist)
