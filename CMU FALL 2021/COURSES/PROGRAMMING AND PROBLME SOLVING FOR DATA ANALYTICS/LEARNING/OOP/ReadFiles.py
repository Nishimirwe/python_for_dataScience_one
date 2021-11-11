# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:05:21 2021

@author: Jean Paul Nishimirwe
"""

def main():
    readfile=open("file.txt", 'r')
    lines=readfile.read()
    arr=lines.split("\n")[:-1]
    s=0
    for line in arr:
        li=[int(i) for i in line.split(" ")]
        s=s+sum(li)
    
    out=open("fileOut.txt",'w')
    if s > 200:
        out.write("Sum is large enough: "+str(s))
    else:
        out.write("Sum is too low enough: "+str(s))
    
    readfile.close()
    out.close()
main()