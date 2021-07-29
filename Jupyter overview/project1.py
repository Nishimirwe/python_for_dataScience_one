import paulmodule

f=paulmodule.fib(8)
print(f"fib({8})={f}")
print("Imana irakarama")
for i in range(10):
    print("I love you")

li=[i for i in range(1,50)]
arr=filter(paulmodule.isEven,li)
arr=list(arr)
print(len(arr))

print(__name__)

# I am going to use Node class from paul module
lON=[]
node=paulmodule.Node(45)
lON.append(node)
node1=paulmodule.Node(70)
lON.append(node1)
node.show()
print(f"index is {node.index}")

print(f"second node is {node1.data}, and its index is {node1.index}, now having the total of {paulmodule.Node.number+1} nodes")
for i in lON:
    print(i.data," ",end=''),
    
    
print("----------------------------------------------------------------------")
    
# let me use revString method from my module "paulmodule"

str=input("Enter an string to reverse it:  ")
print(paulmodule.revString(str))

# asking for help using showHelp methoh in paulmodule
paulmodule.showHelp()
