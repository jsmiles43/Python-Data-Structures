#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:28:31 2017

@author: josephmiles
"""
import string

ALPHABET = list(string.ascii_lowercase)

class Trie:
    
    def __init__(self):
       	self.head = Node('TRIE')
        self.alphabet = ALPHABET
       	
    



    def addWord(self, word):
        p = self.head
        for letter in word:
        	index = self.alphabet.index(letter)
        	if not p.children[index]:
        		p.children[index] = Node(letter)
        	else:
        		child = p.children[index]
        		p = child
        	

    def printTree(self, head):
    	for i in range(26):
    		if head.children[i] == None:
    			return
    		self.printTree(head.children[i])
    		print(head.data)
        
        
    
        
        

        
        
        
        
        
        
        
        
        
        
class Node:
    def __init__(self, letter):
        self.data = letter
        self.children = 26 * [None]

    def __str__(self):
        return str(self.data)
        
        
        
        
        

trie = Trie()
trie.addWord('tree')  
trie.printTree(trie.head)     
        
     
        
        
        

        
        
        
        
        
        
        
        