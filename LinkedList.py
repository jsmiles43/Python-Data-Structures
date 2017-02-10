# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    
    def __str__(self):
        '''for testing purposes'''
        p = self.root
        st = ''
        while (p != None):
            st = st + ' ' + str(p.data)
            p = p.next
        return st
        
    def addNode(self, n):
        if self.root == None:
            self.root = n
        else:
            p = self.root
            while p.next != None:
                p = p.next
            p.next = n





class Node:
    
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
        
    def getData(self):
        return self.data
    
    def setData(self, d):
        self.data = d
        
        
        
        
x  = Node(3, None)



linkedlist = LinkedList()
linkedlist.addNode(x)
linkedlist.addNode(Node(5, None))

print(linkedlist.__str__())