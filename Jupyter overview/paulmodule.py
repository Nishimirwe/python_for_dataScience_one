# the following function takes an integer paremeter and return it fibonacci value
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)



# the following  takes to numbers and return one to the power of another
def power(base,exp):
    if exp==0:
        return base
    elif base==0:
        return False
    elif base==1:
        return 1
    else:
        return base*power(base,exp-1)
    
    
# Method to check odd or even number
def isEven(n):
    return n%2==0
if __name__=="__main__":
    print("I am open")
if __name__!="__main__":
    print()
    print()
    print("paulmodule is imported")
    print()
    print()

class Node:
    number=-1;
    def __init__(self,v):
        print("Node is declared")
        self.data=v
        Node.number+=1
        self.index=Node.number
        self.next=None
        
    def show(self):
        print(self.data)
 