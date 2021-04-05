stack = []
size = input("Stack size : ")
while not size.isdigit():
    size = input("Invalid input, please enter an integer : ")
size = int(size)
e=[]
while 1: 
    no = input("\nPress:\n1 to pop from stack\n2 to push to stack\n3 to view your stack\n4 to exit\n")
    if no.isdigit():
        if no == "1":
            if stack!=[]:
                print(stack.pop(),"has been popped.")
            else:
                print("Stack underflow")
        elif no == "2":
            if len(stack)<size:
                item = input("Enter the item to pushed : ")
                stack.append(item)
            else:
                print("Stack overflow")
        elif no == "3":
            print("The contents of your stack are")
            for e in reversed(stack):  
                print(e,end=" ")
        elif no == "4":
            break
    else:
        print("Invalid input")
