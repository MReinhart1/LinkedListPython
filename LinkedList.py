"""
---------------------------------
Assignment 3 "Linked list"
Student Name: Michael Reinhart
Student Number:  20001556
Date Modified : March 17 2017
---------------------------------
"""
import urllib.request


# Reads in a web page and assigns each row to a node in our linked list
def readHtml():
    toDoList = None
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/todo.txt")
    html = response.readline()
    data = html.decode('utf-8').split()
    toDoList = addIn(toDoList, data)

    while len(html) != 0:
        html = response.readline()
        data = html.decode('utf-8').split()
        toDoList = addIn(toDoList, data)

    # This will 'Delete' the first item in our linked list, which is the empty data set
    toDoList = toDoList['next']
    return toDoList


# Used for testing purposes, this prints out the contents of the linked list
def printList(aList):
    ptr = aList
    while ptr != None:
        print(ptr['data'], "->", end="")
        ptr = ptr['next']

    print("None")


# This function adds a new node containing data to the beggining of a linked list and returns the new linked list
def addIn(aList, value):
    newNode = {}
    newNode["data"] = value
    newNode["next"] = aList
    return newNode


def addToHead(linkedList, value):
    newnode = {}
    newnode["data"] = value
    # set the next pointer of this new node to the head of the list, linkedList
    # newnode is now the head of the list, so we return this node (which is
    # connected to the rest of the list
    newnode["next"] = linkedList
    return newnode


# This 'removes' a task from the to do list and moves it to the did it list

def executeTask(toDo, Task, didIt):
    ptr = toDo
    while ptr['next'] != None:
        if ptr['data'] == None:
            print("This is not in the todo list")
            break

        elif ptr['next']["data"][0:-3] == Task:
            # First gets rid of the task from the to do list
            didIt, ptr['next'] = addToHead(didIt, ptr['next']['data']), ptr['next']['next']

            # After the task is deleted from the to do list, it is added to the DidIt list
            # ASK IF I CAN DO IT THIS WAY OR IF I AM NEVER ALOUD TO USE A NEW NODE
            return toDo, didIt



# This function will open the command file and run the program appropriately
def Driver():
    # Initializing the toDo and didIt lists
    toDoList = readHtml()
    didItList = None

    # This runs through for the first instruction on the command list
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/driver.txt")
    html = response.readline()
    data = html.decode('utf-8').split()

    if data[0] == 'PrintToDo':
        print("Todo list:")
        printList(toDoList)


    elif data[0] == 'PrintDidIt':
        print("Didit list:")
        printList(didItList)


    elif data[0] == 'ExecuteTask,':
        finishedTask = data[1:-1]
        toDoList, didItList = executeTask(toDoList, finishedTask, didItList)

    elif data[0] == 'AddTask,':
        task = data[1:]
        toDoList = addIn(toDoList, task)

    else:
        print("Sorry that's not a valid function")

    # After the first command is made, this section of code will carry out the remainder of the commands
    while len(html) != 0:
        html = response.readline()
        data = html.decode('utf-8').split()
        if len(html) != 0:

            if data[0] == 'PrintToDo':
                print("Todo list:")
                printList(toDoList)

            elif data[0] == 'PrintDidIt':
                print("Didit list:")
                printList(didItList)

            elif data[0] == 'ExecuteTask,':
                finishedTask = data[1:-1]
                toDoList, didItList = executeTask(toDoList, finishedTask, didItList)

            elif data[0] == 'AddTask,':
                task = data[1:]
                toDoList = addIn(toDoList, task)

            else:
                print("Sorry that's not a valid function")


Driver()

