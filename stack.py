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


class Stack:

    def __init__(self):
        self.lst_instance = SinglyLinkedList()


    def pop(self):
        return self.lst_instance.removeAt(0)

    def push(self, value):
        self.lst_instance.insertAt(value, 0)

stack = Stack()

stack.push("a")
stack.push("b")
stack.push("c")

print(stack.pop())
print(stack.pop())
print(stack.pop())


class Stack:
    def __init__(self):
        self.lst_instance = []

    def pop(self):
        return self.lst_instance.pop()

    def push(self, value):
        self.lst_instance.append(value)


stack = Stack()

stack.push("a")
stack.push("b")
stack.push("c")

print(stack.pop())
print(stack.pop())
print(stack.pop())
