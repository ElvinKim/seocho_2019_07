import time

class Node:
    nodeNext = None
    nodePrev = ''
    objValue = ''
    blnHead = False
    blnTail = False
    def __init__(self, objValue = '', nodeNext = None, blnHead = False, blnTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.blnHead = blnHead
        self.blnTail = blnTail
    def getValue(self):
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue
    def getNext(self):
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    def isHead(self):
        return self.blnHead
    def isTail(self):
        return self.blnTail


class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeTail = Node(blnTail=True)
        self.nodeHead = Node(blnHead=True, nodeNext=self.nodeTail)
        
    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1
        
    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()
        
    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end=" ")
        print("")
        
    def getSize(self):
        return self.size


total_len = 1000000
val_insert = 1000

list1 = SinglyLinkedList()

for i in range(total_len):
	list1.insertAt(i, 0)

start_time = time.time()
list1.insertAt(val_insert, int(total_len / 2))
print(time.time() - start_time)

start_time = time.time()
list1.insertAt(val_insert, int(total_len / 3))
print(time.time() - start_time)

start_time = time.time()
list1.insertAt(val_insert, int(total_len / 4))
print(time.time() - start_time)
