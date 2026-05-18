"""
ce code a ete pris sur un site que je me souvien plus
donc si se vous ammuse vous poserez des questions la dessus
de modification sur le code original on ete faite
"""


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

    def traverseFromFront(self):
        temp = self.head
        while temp:
            temp = temp.prochain

    def traverseFromEnd(self):
        temp = self.head
        while temp.prochain is not None:
            temp = temp.prochain
        tail = temp
        while tail is not None:
            tail = tail.avant

    def search(self, searchItem):
        temp = self.head

        while temp.prochain is not None and temp.info is not searchItem:
            temp = temp.prochain

        return temp


all_frame = Liste_Frame()
