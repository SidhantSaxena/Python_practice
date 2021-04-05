queue = []
i=0
size = input("Queue size : ")
while not size.isdigit():
    size = input("Invalid input, please enter a number : ")
size = int(size)    
while i==0:
    no=input("\nPress:\n1 for dequeueing element\n2 for enqueueing element\n3 for viewing your queue\n4 to exit\n")
    if no.isdigit():
        if no == "1":
            if queue!=[]:
                 print(queue.pop(0),"has been dequeued")
            else:
                print("Queue is empty")
        elif no == "2":
            if len(queue)<size:
                item = input("Enter the item you wish to enqueue : ")
                queue.append(item)
                print(item,"has been enqueued")
            else:
                print("Limit exceeded")
        elif no == "3":
            print(" ".join(queue))
        elif no == "4":
            i=2
    else:
        print("Invalid input")
