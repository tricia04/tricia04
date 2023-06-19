def heapify(arr, arr1, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        arr1[i], arr1[largest] = arr1[largest], arr1[i]

        heapify(arr, arr1, n, largest)


def buildHeap(arr, arr1, n):
    startIdx = n // 2 - 1

    for i in range(startIdx, -1, -1):
        heapify(arr, arr1, n, i)


def printHeap(arr, arr1, n):
    for i in range(n):
        print(arr[i], end=" ")
        print(arr1[i], end=" ")
    print()


class tree:
    def __init__(self):
        self.head = None
        self.level = 0

    def first(self, top):
        if top == None:
            return
        else:
            print(top.name)
            self.first(top.child)

    def flev(self, top, k):
        if top.name == k:
            return self.level
        if top.child != None:
            self.level += 1
            lv = self.flev(top.child, k)
            if lv == None:
                if top.sibling != None:
                    return self.flev(top.sibling, k)
            return lv

        if top.child == None and top.sibling != None:
            return self.flev(top.sibling, k)
        if top.child == None and top.sibling == None:
            self.level -= 1
            return

    def reset(self):
        self.level = 0


class node:
    def __init__(self, k):
        self.name = k
        self.child = None
        self.sibling = None


class Node:

    def __init__(self, name, reg, num):
        self.name = name
        self.reg = reg
        self.num = num
        self.sal = 0
        self.next = None
        self.prev = None

    def addsal(self, sal):
        self.sal = sal


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_name, new_reg, new_num):

        new_node = Node(new_name, new_reg, new_num)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        new_node.prev = last

        return

    def printdata(self, name):
        current = self.head

        if self.head is None:
            print("EMPTY")
            return

        while current:
            if current.name == name:
                print("NAME: ", current.name)
                print("REGISTER NUMBER: ", current.reg)
                print("MOBILE NUMBER: ", current.num)
                print("Current Salary: ", current.sal)
                return

            current = current.next

        print("Employee not found.")


def calc(arr, arr1, n, arrs, arrh, comp, llist):
    arro = []

    for i in range(n):
        al = comp.flev(comp.head, arr1[i])
        comp.reset()
        temp = llist.head
        val = arrs[al] + arr[i] * arrh[al]
        while temp != None:
            if temp.name == arr1[i]:
                temp.addsal(val)
                break
            temp = temp.next
        arro.append(val)
    return arro


if name == 'main':
    comp = tree()
    comp.head = node("John")
    comp.head.child = node("Alan")
    comp.head.child.sibling = node("Alex")
    comp.head.child.sibling.sibling = node("Andrew")
    comp.head.child.child = node("Gareth")
    comp.head.child.child.sibling = node("Gary")
    comp.head.child.sibling.child = node("Luffy")
    comp.head.child.sibling.sibling.child = node("Zoro")
    comp.head.child.sibling.sibling.child.child = node("Nami")
    comp.head.child.sibling.sibling.child.child.sibling = node("Robin")

    arr = [1, 3, 5, 6, 13,
           10, 9, 8, 15, 17]
    arr1 = ["John", "Alan", "Alex", "Andrew", "Gareth", "Luffy", "Zoro", "Nami", "Robin", "Gary"]

    n = len(arr)

    buildHeap(arr, arr1, n)

    printHeap(arr, arr1, n)

    arrs = [50000, 30000, 20000, 10000, 8000]
    arrh = [250, 200, 150, 100, 80]

    llist = DoublyLinkedList()

    llist.append("John", 201, 9998887776)
    llist.append("Nami", 219, 8887786734)
    llist.append("Alan", 212, 7778889990)
    llist.append("Alex", 203, 7768859994)
    llist.append("Andrew", 204, 677581290)
    llist.append("Gareth", 206, 9874883390)
    llist.append("Luffy", 310, 9977654809)
    llist.append("Zoro", 312, 98768889990)
    llist.append("Gary", 207, 9879879875)
    llist.append("Robin", 202, 69877896734)

    arro = calc(arr, arr1, n, arrs, arrh, comp, llist)
    ch = 1

    while ch == 1:
        print(
            "Enter 'S' for salary report \nEnter 'Top' for top employee of the month \nEnter 'D' for details of an employee \n")
        inp = input()
        if inp == "S":
            for i in range(n):
                print(arr1[i], " ", arro[i])
        elif inp == "Top":
            print("------Top Employee of the Month is ", arr1[0], "------")
        elif inp == "D":
            p = input("Enter employee name:")
            llist.printdata(p)

        ch = int(input("enter 1 to continue:"))