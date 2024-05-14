from InitialFile import InitialFile

class Node:
    def __init__(self, id: int):
        self.id = id

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return False


class Source(Node):
    def __init__(self, id: int, itemsCapacity: list):
        super().__init__(id)
        self.itemsCapacity = itemsCapacity

    def getCapacity(self, itemId) -> int:
        if itemId < len(self.itemsCapacity):
            return self.itemsCapacity[itemId]
        else:
            print("item id not found")
            exit()

class Edge:
    def __init__(self, id: int, start: int, end: int, itemsCost: list):
        self.id = id
        self.start = start
        self.end = end
        self.itemsCost= itemsCost

    def getCost(self, itemId) -> int:
        if itemId < len(self.itemsCost):
            return int(self.itemsCost[itemId])
        else:
            print("item id not found")
            exit()


class Destination(Node):
    def __init__(self, id: int, itemsDemand: list):
        super().__init__(id)
        self.itemsDemand = itemsDemand

    def getDemand(self, itemId) -> int:
        if itemId < len(self.itemsDemand):
            return self.itemsDemand[itemId]
        else:
            print("item id not found")
            exit()


class Graph:
    def __init__(self, initialFile:InitialFile):
        self.nodeList = list()
        self.sourceList = list()
        self.edgeList = list()
        self.destinationList = list()
        self.p = initialFile.p
        self.file = initialFile.file
        self.fillList(initialFile)

    def getComingEdgeToNode(self, node:Node) -> list:
        temp = list()
        for edge in self.edgeList:
            if edge.end == node.id:
                temp.append(edge)
        return temp

    def getExitingEdgeToNode(self, node:Node) -> list:
        temp = list()
        for edge in self.edgeList:
            if edge.start == node.id:
                temp.append(edge)
        return temp

    def getNormalNode(self) -> list:
        temp = list()
        for node in self.nodeList:
            boolean = True
            for source in self.sourceList:
                if node == source:
                    boolean = False
            for destination in self.destinationList:
                if node == destination:
                    boolean = False
            if boolean:
                temp.append(node)
        return temp



    def fillList(self, initialFile:InitialFile):
        if self.p == 0:
            self.fillListAggregated(initialFile)
        elif self.p == 1:
            self.fillListDisaggregated(initialFile)

    def fillListAggregated(self, initialFile:InitialFile):
        self.itemNumber = initialFile.getItemsNumber()
        self.nodeNumber = initialFile.getNodesNumber()
        for node in initialFile.getNodesBody():
            temp = node.split()
            self.nodeList.append(Node(int(temp[0])))

        for source in initialFile.getSourcesBody():
            temp = source.split()
            a = 0
            for i in range(self.itemNumber):
                a += int(temp[1 + i])
            self.sourceList.append(Source(int(temp[0]), [a]))

        for edge in initialFile.getEdgesBody():
            temp = edge.split()
            a = 0
            for i in range(self.itemNumber):
                a += int(temp[3 + i])
            self.edgeList.append(
                Edge(int(temp[0]), int(temp[1]), int(temp[2]), [a/self.itemNumber]))

        for destination in initialFile.getDestinationsBody():
            temp = destination.split()
            a = 0
            for i in range(self.itemNumber):
                a += int(temp[1 + i])
            self.destinationList.append(Destination(int(temp[0]), [a]))
        self.itemNumber = 1

    def fillListDisaggregated(self, initialFile:InitialFile):
        self.itemNumber = initialFile.getItemsNumber()
        self.nodeNumber = initialFile.getNodesNumber()
        for node in initialFile.getNodesBody():
            temp = node.split()
            self.nodeList.append(Node(int(temp[0])))

        for source in initialFile.getSourcesBody():
            temp = source.split()
            self.sourceList.append(Source(int(temp[0]), [int(temp[1 + i]) for i in range(self.itemNumber)]))

        for edge in initialFile.getEdgesBody():
            temp = edge.split()
            self.edgeList.append(
                Edge(int(temp[0]), int(temp[1]), int(temp[2]), [int(temp[3 + i]) for i in range(self.itemNumber)]))

        for destination in initialFile.getDestinationsBody():
            temp = destination.split()
            self.destinationList.append(Destination(int(temp[0]), [int(temp[1 + i]) for i in range(self.itemNumber)]))

