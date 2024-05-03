class MyLinkedList:

    def __init__(self):
        self.linkedList: List[int] = []

    def get(self, index: int) -> int:
        if index < len(self.linkedList):
            return self.linkedList[index]
        else:
            print('get: ', index, self.linkedList)
            return -1

    def addAtHead(self, val: int) -> None:
        self.linkedList = [val] + self.linkedList

    def addAtTail(self, val: int) -> None:
        self.linkedList.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.linkedList):
            self.linkedList.insert(index, val)
        elif index == len(self.linkedList):
            self.linkedList.append(val)
        else:
            print('addAtIndex: ', index, self.linkedList)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.linkedList):
            self.linkedList.pop(index)
        else:
            print('deleteAtIndex: ', index, self.linkedList)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
