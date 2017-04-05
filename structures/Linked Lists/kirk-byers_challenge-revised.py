inp = open('./input.txt', 'r')
N, K = (int(x) for x in inp.readline().split(' '))
salePrices = [int(x) for x in inp.readline(). split(' ')]
inp.close()

class Window(object):
    def __init__(self, inp, windowSize):
        self.bodyValue = 0
        self.head = None
        self.tail = Node(0, inp[0], inp[1])
        for i in range(2,windowSize):
            self.pushUnit(inp[i])
        
    def value(self):
        if self.head == None:
            return self.tail.value
        return self.bodyValue + self.head.value + self.tail.value
    
    def pushUnit(self, unit):
        if unit == self.tail.endUnit and self.tail.direction == 0:
            self.tail.grow(unit)
        elif unit > self.tail.endUnit and self.tail.direction == 1:
            self.tail.grow(unit)
        elif unit < self.tail.endUnit and self.tail.direction == -1:
            self.tail.grow(unit)
        else:
            newNode = Node(self.tail.end, self.tail.endUnit, unit)
            if self.head == None:
                self.tail.next = newNode
                self.head = self.tail
                self.tail = newNode
            else:
                self.bodyValue += self.tail.value
                self.tail.next = newNode
                self.tail = newNode
            
    def popUnit(self):
        self.head.shrink()
        if self.head.length() <= 0:
            self.head = self.head.next
            self.bodyValue -= self.head.value
            
        
class Node(object):
    def __init__(self, startIndex, startUnit, endUnit):
        if startUnit > endUnit:
            self.direction = -1
        elif startUnit < endUnit:
            self.direction = 1
        elif startUnit == endUnit:
            self.direction = 0
        
        self.start = startIndex

        self.end = startIndex + 1
        self.endUnit = endUnit
        
        self.value = self.direction
        
        self.next = None # Node
        
    def length(self):
        return self.end - self.start
    
    def grow(self, unit):
        self.end += 1
        self.endUnit = unit
        self.value += self.length() * self.direction
        
    def shrink(self):
        self.value -= self.length() * self.direction
        self.start += 1

#Record output to file
f = open('./output.txt', 'w')

#Set up first window
currentWindow = Window(salePrices, K)

f.write(str(currentWindow.value()) + '\n')

#Iterate the rest of windows in N
for i in range(K, N):
    currentWindow.pushUnit(salePrices[i])
    currentWindow.popUnit()
    f.write(str(currentWindow.value()) + '\n')

f.close()