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

    
