# [ 45 , next(85) ]----[85 , next(96) ]----[96 , next(946) ]------[946 , next(15) ]-------[15 , next(None) ]
# [ 45 , next(85) ]----[85 , next(96) ]----[96 , next(5) ]------[ 5 , next(946) ]------[946 , next(15) ]-------[15 , next(None) ]


class Linked_List():
    
    class Node:
        def __init__(self , element , next ):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addfirst(self,e):
        node = self.Node(e,None)
        if self.size==0:
            self.head=node
            self.tail=node
        else:
            node.next = self.head
        self.head = node
        self.size+=1
    
    def addlast(self,e):
        node = self.Node(e,None)
        if self.size==0:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
        self.tail = node
        self.size+=1        
    
    def removeFirst(self):
        if self.size==1:
            self.head = self.head.next
            self.tail=None
        elif self.size>1:
            self.head = self.head.next
        self.size-=1  

    def removeLast(self):
        if self.size>1:
            self.tail=None
            h = self.head
            for _ in range(self.size-2):
                h = h.next
            h.next = None
            self.tail=h
        elif self.size==1:
            self.tail=None
            self.head=None     
        self.size-=1

    def addAt(self,e,a):
        node=self.Node(e,None)
        th=self.head
        if self.size==0:
            self.head=node
            self.tail=node
        elif a>0 :
            for _ in range(a-1):
                th=th.next
            x=th.next
            th.next=node
            node.next=x
        else:
            self.addfirst(e)   
             

        self.size+=1    

    def dispay(self):
        thead=self.head
        while thead:
            print(f'{thead.element}-->',end=" ")
            thead = thead.next
        print()
        if self.size==0:
            print("empty linked list") 


link = Linked_List()
link.addfirst(45)
link.addfirst(35)
link.addfirst(56)
link.addlast(23)
link.addAt(5,9)
link.dispay()


