class Frame:
    def __init__(self, data=None, prev=None, next=None):
        self.info = data
        self.prochain = next
        self.avant = prev


class Liste_Frame:
    def __init__(self):
        self.head = None
        self.traverser = True
        self.taille = 0

    def insertFront(self, val):
        newNode = Frame(data=val)
        newNode.prochain = self.head
        if self.head is not None:
            self.head.avant = newNode
        self.head = newNode
        # print("Added {} at the front".format(val))

    def insertEnd(self, val):
        newNode = Frame(data=val)
        if self.head is None:
            self.insertFront(val)

        temp = self.head
        while temp.prochain is not None:
            temp = temp.prochain
        temp.prochain = newNode
        newNode.avant = temp
        self.taille += 1
        # print("Added {} at the end".format(val))

    def traverseFromFront(self):
        temp = self.head
        while temp:
            #   print("{}\t".format(temp.info))
            temp = temp.prochain

        # def traverseFromFront_one(self,current):
        #     temp = current
        #     print("Traversing from head:\t",end="")
        #     print("{}\t".format(temp.info))
        #     temp = temp.prochain
        #     print()
        #     return temp

    def traverseFromEnd(self):
        temp = self.head
        print("Traversing from Tail:\t", end="")
        while temp.prochain is not None:
            temp = temp.prochain
        tail = temp
        while tail is not None:
            print("{}\t".format(tail.info), end="")
            tail = tail.avant
        print()

    # def insertAfter(self,searchItem, value):
    #   newNode = Frame(data=value)

    #   temp = self.head
    #   while temp.prochain is not None and temp.info is not searchItem:
    #     temp = temp.prochain

    #   newNode.prochain = temp.prochain
    #   temp.prochain = newNode
    #   newNode.avant = temp

    #   if newNode.prochain is not None:
    #     newNode.prochain.prev = newNode
    #   print("Inserted {} after node {}".format(value,searchItem))

    # def insertBefore(self,searchItem, value):
    #   newNode = Frame(data=value)

    #   temp = self.head
    #   while temp.prochain is not None and temp.prochain.data is not searchItem:
    #     temp = temp.prochain

    #   newNode.prochain = temp.prochain
    #   temp.prochain = newNode
    #   newNode.avant = temp

    #   if newNode.prochain is not None:
    #     newNode.prochain.prev = newNode
    #   print("Inserted {} before node {}".format(value,searchItem))

    def search(self, searchItem):
        temp = self.head

        while temp.prochain is not None and temp.info is not searchItem:
            temp = temp.prochain

        print("Deleted Node\t{}".format(searchItem))
        return temp


all_frame = Liste_Frame()
# doublyLinkedList = Liste_Frame()
# doublyLinkedList.insertFront(5)
# doublyLinkedList.insertFront(6)
# doublyLinkedList.insertFront(7)
# doublyLinkedList.insertEnd(9)
# doublyLinkedList.insertEnd(10)
# doublyLinkedList.insertAfter(5, 11)
# doublyLinkedList.insertBefore(5, 20)
# doublyLinkedList.traverseFromFront()
# doublyLinkedList.traverseFromEnd()
# doublyLinkedList.searchAndDelete(7)
# doublyLinkedList.traverseFromFront()
# doublyLinkedList.traverseFromEnd()
