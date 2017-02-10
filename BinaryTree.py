#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:28:14 2017

@author: josephmiles
"""

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        
    def addNode(self, root, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if root is None:
                root = Node(value)
            elif value <= root.data:
                root.left = self.addNode(root.left, value)
            elif value > root.data:
                root.right = self.addNode(root.right, value)
        return root
            
    def removeNode(self, root, value):
        if root is None: 
            return root
        elif root.data > value:
            root.left = self.removeNode(root.left, value)
        elif root.data < value:
            root.right = self.removeNode(root.right, value)
        elif root.data == value:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                least = self.findMin(root.right)
                root.data = least.data
                root.right = self.removeNode(root.right, least.data)
                return least
        return root  
                
                
    def findMin(self, root):
        if (root.left is None):
            return root
        else:
            return self.findMin(root.left)
            
    def traverseTreeInfix(self, root):
        if root is None:
            return root
        if root.left is not None:
            self.traverseTreeInfix(root.left)
        print(root.data)
        if root.right is not None:
            self.traverseTreeInfix(root.right)
             
    def traverseTreePrefix(self, root):
        if root is None:
            return root
        print(root.data)
        if root.left is not None:
            self.traverseTreePrefix(root.left)
        if root.right is not None:
            self.traverseTreePrefix(root.right)
    
    def traverseTreePostfix(self, root):
        if root is None:
            return root
        if root.left is not None:
            self.traverseTreePostfix(root.left)
        if root.right is not None:
            self.traverseTreePostfix(root.right)
        print(root.data)

            
            
            
            
            
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

        
        
        
        
        
        
btree = BinaryTree()     
btree.addNode(btree.root, 10)
btree.addNode(btree.root, 12)
btree.addNode(btree.root, 8)
btree.addNode(btree.root, 20)
btree.addNode(btree.root, 1)
btree.addNode(btree.root, 11)

btree.traverseTreePostfix(btree.root)



        
        
        
        
        
        
        
        
        
        
        
        
        
        