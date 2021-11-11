import allinone as aio

mh=aio.MaxHeap(5)
mh.addNode(34)
mh.addNode(20)
mh.addNode(40)
mh.addNode(14)
mh.addNode(36)
mh.increaseHeap(5)
mh.addNode(2)
mh.addNode(90)
mh.addNode(75)
print(mh.getLarge())
mh.show()

print(f"Delete : {mh.extractMax()}")

mh.show()

print("-----------------------------------")
print(f"Capacity: {mh.getCapacity()}")
