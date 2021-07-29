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
    print("I am hired")
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


# I am gon code a function that takes string as a parameter and returns its inversed string

def revString(str):
    if len(str)==1:
        return str
    return str[-1]+revString(str[:-1])

# this function is going to give help about python in built
def showHelp():
    print("Strings")
    print()
    print()
    print("Capitalize a string: string.upper()")
    print("Lower a string: string.lower()")
    print()
    print()
    print("Lists")
    print()
    print()
    print("creating a list: list_variable=list() OR list_variable=[]")
    print("Sorting a list Ascending order: list.sort()")
    print("Sroting a list Descending order: list.sort(reverse=True)")
    print("Reversing a string: list.reverse()")
    print("Adding new element in a list: list.append(value)")
    print("Inserting a new Element at a certain position: list.insert(position,value)")
    print("Removing an item from a list: list.remove(item)")
    print("Removing all items from the list: list.clear()")
    
 