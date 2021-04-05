class linked_list:
    class Node:
        def __init__(self,element,nex=None):
            self.element=element
            self.nex=nex

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def addFirst(self,e):
        node = self.Node(e)
        if self.size==0:
            self.head=node
            self.tail=node
        elif self.size>0:
            node.nex=self.head
        self.head = node
        self.tail.nex=self.head  #circle linked_list
        self.size+=1

    def addLast(self,e):
      node = self.Node(e)
      if self.size==0:
        self.head=node
        self.tail=node
      elif self.size>0:
        self.tail.nex=node
      self.tail=node
      self.tail.nex=self.head  #circle linked_list
      self.size+=1  

    def removeHead(self):
      if self.size==0:
        self.tail=None
        self.head=None
      else:
        self.head=self.head.nex
      self.size-=1
      self.tail.nex=self.head

    def display(self):
        th=self.head
        if self.size>0:
            c=0
            while th:
                print(th.element,"--->",end="")
                if th.element==self.tail.nex.element and c==self.size:
                    break
                th=th.nex
                c+=1
        else:
            print("Empty Linked list")
        print()

link=linked_list()
link.addFirst(23)
link.display()
link.addFirst(24)
link.display()
link.addLast(26)
link.removeHead()
link.display()
link.addFirst(287)
link.display()
link.removeHead()
link.display()
