# This a module developed by Jean Paul (A software Engineer)
# His main purpose was to put almost all datas tructures and their algorithms in one module --
# To simplify life for himself and other programmers who might be interested to use this module.

# Data structures that are in here are like:
                # Stack
                # Queue
                # Linked list as LList:
                            # Singly Linked List
                            # Singly circular Linked List
                            # Doubly Linked List
                            # Doubly Circular Linked List
                            
                # Graphs:
                            # DFS(Depth First Search)
                            # BFS(Breadth First Search)
                        
                        
# The module also contains some useful functions used in every day coding jobs
            # power(a,b), a to the power of b
            # revString(string), reversing a string
            # fib(number), fibonacci serie number of a given order (number)
            # fact(number), factorial of a number
            # isEven(number), return True if number is even , otherwise returns False
            # isOdd(number), return True if number is odd, otherwise False
            # isPrime(number), return True if number is prime number, otherwise False
            # isPalindrome(string), return True if a string is palindrome, otherwise false
            # isAnagram(string1,string2), return True if string1 is anagram of string2 (string1 is formed by rearranging string2)
       
    # Node for singly linked List
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
        
# A linked List which is using above Node class

class SLList:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.head==None

    def append(self, value):
        node=Node(value)
        if(self.isEmpty()):
            self.head=self.tail=node
            self.length+=1
        else:
            self.tail.next=node
            self.tail=node
            self.length+=1

    def show(self):
        if self.isEmpty():
            print(f"List is empty")
        else:
            nav=self.head
            while nav:
                print(f"{nav.data} ",end='')
                nav=nav.next
            print()
            print(f"size: {self.length}")
    
    def toList(self):
        if self.isEmpty():
            return False,"List is empty"
        else:
            li=list()
            nav=self.head
            while nav:
                li.append(nav.data)
                nav=nav.next
            return li
        
    def addFirst(self,value):
        node=Node(value)
        node.next=self.head
        self.head=node
        self.length+=1

    def insert(self,value,pos):
        if pos<0 or pos>self.length:
            print("Invalid position")
        elif pos==0:
            self.addFirst(value)
        elif pos==self.length:
            self.append(value)
        else:
            node=Node(value)
            i=1;
            nav=self.head
            while i<pos:
                nav=nav.next
                i+=1
            node.next=nav.next
            nav.next=node
            self.length+=1

    def clear(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def sort(self):
        li=self.toList()
        li.sort()
        self.clear()
        for i in li:
            self.append(i)

    def sortAsc(self):
        li=self.toList()
        li.sort()
        self.clear()
        for i in li:
            self.append(i)
            
            
    def sortDesc(self):
        li=self.toList()
        li.sort(reverse=True)
        self.clear()
        for i in li:
            self.append(i)
            
    def reverse(self):
        li=self.toList()
        li.reverse()
        self.clear()
        for i in li:
            self.append(i)
            
    def deleteFirst(self):
        if self.isEmpty():
            print("List head in None")
        else:
            x=self.head.data
            self.head=self.head.next
            self.length-=1
            return x
                  
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            nav=self.head
            t=None
            while nav!=self.tail:
                t=nav  
                nav=nav.next
            t.next=None
            self.tail=t
            self.length-=1
            return nav.data

    def deleteAt(self,pos):
        if pos<0 or pos>self.length-1:
            return -1
        elif pos==0:
            self.deleteFirst()
        elif pos==self.length-1:
            self.pop()
        else:
            i=1
            nav=self.head
            while i<pos:
                nav=nav.next
                i+=1
            t=nav.next
            x=t.data
            nav.next=t.next
            self.length-=1
            return x
            
 #-----------------------------------------------------------------------------------------------------                 
                
                
# Function to take a python list or tupple and turn it to SLList
def toSLList(li):
    if len(li)==0:
        print("Cannot take empty list")
    else:
        sllist=SLList()
        for i in li:
            sllist.append(i)
        return sllist
    

# Returning the fibonacci serie number on any order
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
    
#Returning the factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
#Calculate the gcd of a number
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

#-----------------------------------------------------------------------------------------------------

# I am going to code a function to download image, by passing name and its online link
# Note that this function works after importing requests

def downloadImg(name,url):
    print("Hope you have imported requests library. If not, do it first")
    img_res=rq.get(url)
    img_res.status_code
    img_data=img_res.content
    with open(name,'wb') as f:
        f.write(img_data)
        
#-----------------------------------------------------------------------------------------------------
        
# I am gon import as many libraries as possible
def importNumpy():
    import numpy as np
    print("numpy is imported as np")
    
def importPandas():
    import pandas as pd
    print("Pandas is imported as pd")
    
def importMatPlotLib():
    import matplotlib.pyplot as plt
    print("matplotlib is imported as plt")
    
def importSeaBorn():
    import seaborn as sb
    print("seaborn is imported as sb")
    
def importRequests():
    import requests as rq
    print("requests is imported as rq")
    
def importCV2():
    import cv2
    print("cv2 is imported as cv2")
    
def importBeautifulSoup():
    import bs4
    print("beautifulsoup is imported as bs4")
"""
Here, I am going to code a queue data structure using linked list
methods: push(data), pop(), pop(index), clear(), show(), front(), back()
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def isEmpty(self):
        return self.head==None    

    def enq(self,value):
        node=Node(value)
        if self.isEmpty():
            self.head=node
            self.tail=node
            self.length+=1
        else:
            self.tail.next=node
            self.tail=node
            self.length+=1

    def deq(self):
        if self.isEmpty():
            return None
        else:
            t=self.head
            x=t.data
            self.head=t.next
            t.next=None
            self.length-=1
            return x
    
    def clear(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data

    def show(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            nav=self.head
            print("Queue: ",end='')
            while nav:
                print(f"{nav.data} ",end='')
                nav=nav.next
            print()
            print()
            print(f"Details: size is {self.length} => Front is {self.head.data} => Back is {self.tail.data}")


"""
The following class is a stack data structure.
the methods available are: push(data), pop(), clear(), show(), top(), bottom()
""" 
# I my opinion now, I feel like a node with prev and next can be useful in stack implementation. Let me use it.

class stackNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class stack:
    def __init__(self):
        self.t=None
        self.b=None
        self.length=0

    def isEmpty(self):
        return self.t==None

    def push(self,value):
        node=stackNode(value)
        if self.isEmpty():
            self.t=node
            self.b=node
            self.length+=1
        else:
            self.t.next=node
            node.prev=self.t
            self.t=node
            self.length+=1
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            x=self.t.data
            self.t=self.t.prev
            self.t.next=None
            self.length-=1
            return x

    def top(self):
        return self.t.data

    def bottom(self):
        return self.b.data
    
    def show(self):
        if self.isEmpty():
            print("Empty Stack")
        else:
            nav=self.b
            print("Stack: ",end='')
            while nav:
                print(f"{nav.data} ",end='')
                nav=nav.next
            print()
            print()
            print(f"Details: Size is {self.length} => Top is {self.t.data} => Bottom is {self.b.data}")

"""
I am going t code an unbalanced Binary tree
functions available: addNode(value), inOrder(root), postOrder(root), preOrder(root),
 isEmpty(), search(value)

This data structure is going to use a linked representaion rather than array
"""
# I am going to code a function that explains about this BTree

def explainBinaryTree():
    print(""" This Data structure has different methods that do different tasks.
    Briefly abou functions: 
    1. isEmpty() : Check if a tree is empty or not.
    2. getRoot() : it returns the root node of the tree
    3. addNode(int value): This function add a new node on the tree.
    4. size(): returns the total number of nodes available i =n a tree.
    5. searc(value): it searches a value in a tree.
    6. Navigation: inOrder(getRoot), postOrder(getRoot) and preOrder(getRoot)
    """)

# Let me define a Node for Binary tree
class BTNode:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        self.length=0
    
    def isEmpty(self):
        return self.root==None

    def getRoot(self):
        return self.root    
    
    def addNode(self,value):
        node=BTNode(value)
        if self.isEmpty():
            self.root=node
            self.length+=1
        else:
            above=self.root
            nav=self.root
            go=""
            while nav:
                above=nav
                if value <= nav.data:
                    nav=nav.left
                    go="left"
                else:
                    nav=nav.right
                    go="right"
                if nav==None:
                    if go=="left":
                        above.left=node
                        self.length+=1
                        return "Added"
                    else:
                        above.right=node
                        self.length+=1
                        return "Added"

    def size(self):
        return self.length  

    def search(self,value):
        if self.isEmpty():
            return 0
        else:
            nav=self.root
            go=True
            while nav and go:
                if value == nav.data:
                    return value
                elif value < nav.data:
                    nav=nav.left
                else:
                    nav=nav.right

            return 0   
            
    def inOrder(self,r):
        if r:  
            self.inOrder(r.left)
            print(f"{r.data} ",end='')
            self.inOrder(r.right)
    
    def preOrder(self,r):
        if r:
            print(f"{r.data} ",end='')
            self.preOrder(r.left)
            self.preOrder(r.right)

    def postOrder(self,r):
        if r:
            self.postOrder(r.left)
            self.postOrder(r.right)
            print(f"{r.data} ",end='')    

"""
I am going to do minHeap data structure.
"""

def explainMinHeap():
    print("""This is a MinHeap Data structure. This data structure can be used fro solving
    priority queues question. The logic is, the root of the tre is always the smallest element in the tree.
    In addition, it is unsured that parent node is smaller than its children nodes.
    
     This data structure has different functions:
     1. isEmpty()
     2. addNode(value)
     3. pop()
     4. extendHeap(newSiz)
     5. extractMin()
     6. getRoot() = getSmall()
     7. getLast()
      """)

#  Let me have my class
class MinHeap:
    def __init__(self,capacity):
        self.capacity=capacity
        self.length=0
        self.heap=[]

    def isEmpty(self):
        return self.length==0

    def isFull(self):
        return self.length==self.capacity

    def parent(self,index):
        return (index-1)//2

    def right(self, index):
        return (index*2)+2

    def left(self,index):
        return (index*2)+1

    def getRoot(self):
        return self.heap[0]
        
    def getSmall(self):
        return self.heap[0]

    def getLast(self):
        return self.heap[self.length-1]        

    def addNode(self,value):
        if self.isFull():
            print(f"I am sorry, {value} could not be added, because the heap is full")
        else:
            if self.length==0:
                self.heap.append(value)
            else:
                self.heap.append(value)
                self.insertHeapify(self.length)
            self.length+=1

    def insertHeapify(self, index):
        if index > 0 and self.heap[index]<self.heap[self.parent(index)]:
            self.heap[index],self.heap[self.parent(index)]=(self.heap[self.parent(index)], self.heap[index])
            self.insertHeapify(self.parent(index))

    def show(self):
        if self.isEmpty():
            print(f"The Heap is empty.")
        else:
            for i in range(self.length):
                print(f"{self.heap[i]} ",end='')
            print()
            print()
            print(f"Size = {self.length}, Root = {self.getRoot()} and Last = {self.getLast()}")   

    def increaseHeap(self, n):
        self.capacity+=n

    def extractMin(self):
        if not self.isEmpty():
            if len(self.heap) == 1:
                self.length-=1
                return self.heap.pop()
            x=self.heap.pop()
            self.heap[0]=x
            r=self.heap[0]
            self.length-=1
            self.deleteHeapify(0)
            return r
           
        else:
            print("I am sorry, the heap is empty")

    def deleteHeapify(self,index):
        if self.left(index) < self.length and self.right(index) < self.length:
            if self.heap[self.left(index)] < self.heap[index] or self.heap[self.right(index)] < self.heap[index] :
                if self.heap[self.left(index)] <= self.heap[self.right(index)]:
                    self.heap[self.left(index)], self.heap[index]= (self.heap[index],self.heap[self.left(index)])
                    self.deleteHeapify(self.left(index))
                else:
                    self.heap[self.right(index)], self.heap[index]= (self.heap[index],self.heap[self.right(index)])
                    self.deleteHeapify(self.right(index))
                    
        elif self.left(index) < self.length and not (self.right(index) < self.length):
            if self.heap[self.left(index)] < self.heap[index]:
                self.heap[self.left(index)], self.heap[index]= (self.heap[index],self.heap[self.left(index)])
                self.deleteHeapify(self.left(index))

        else:
            pass    




            
            
            


    
            