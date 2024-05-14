class InitialFile:
    def __init__(self, file: str, p: int):
        self.file = file
        with open(file, 'r') as file:
            # Read the lines of the file into a list
            self.lines = file.readlines()
            self.p = p
            self.position = 0


    def checkFormat(self) -> bool:
        if len(self.lines) >= 13:
            self.items = self.getCurrentSectionContent()
            self.itemsNumber = self.items[0].split()[1]
            if len(self.items) == 0 or not self.contains(self.items[0], "ITEMS"):
                return False
            self.getNextSection()

            self.nodes = self.getCurrentSectionContent()
            self.nodesNumber = self.nodes[0].split()[1]
            if len(self.nodes) == 0 or not self.contains(self.nodes[0], "NODES"):
                return False
            self.getNextSection()

            self.edges = self.getCurrentSectionContent()
            self.edgesNumber = self.edges[0].split()[1]
            if len(self.edges) == 0 or not self.contains(self.edges[0], "EDGES"):
                return False
            self.getNextSection()

            self.sources = self.getCurrentSectionContent()
            self.sourcesNumber = self.sources[0].split()[1]
            if len(self.sources) == 0 or not self.contains(self.sources[0], "SOURCES"):
                return False
            self.getNextSection()

            self.destinations = self.getCurrentSectionContent()
            self.destinationsNumber = self.destinations[0].split()[1]
            if len(self.destinations) == 0 or not self.contains(self.destinations[0], "DESTINATIONS"):
                return False
            return True
        else:
            return False

    def contains(self, line: str, string: str):
        if line.find(string) != -1:
            return True
        else:
            return False
    def getNextSection(self):
        currentLine = self.lines[self.position]
        currentLine = currentLine.strip(" ").strip("\n")
        position = self.position
        while len(currentLine) != 0:
            position += 1
            currentLine = self.lines[position]
            currentLine = currentLine.strip(" ").strip("\n")
        self.position = position +1

    def getCurrentSectionContent(self) -> list:
        currentLine = self.lines[self.position]
        currentLine = currentLine.strip(" ").strip("\n")
        position = self.position
        while len(currentLine) != 0 and position != len(self.lines) - 1:
            position += 1
            currentLine = self.lines[position]
            currentLine = currentLine.strip(" ").strip("\n")
        if position == len(self.lines) - 1:
            position += 1
        return self.lines[self.position: position]

    def getItemsNumber(self) -> int:
        return int(self.itemsNumber)

    def getSourcesNumber(self) -> int:
        return int(self.sourcesNumber)

    def getSourcesBody(self) -> list:
        return self.sources[2:]

    def getDestinationsNumber(self) -> int:
        return int(self.destinationsNumber)

    def getDestinationsBody(self) -> list:
        return self.destinations[2:]

    def getNodesNumber(self) -> int:
        return int(self.nodesNumber)

    def getNodesBody(self) -> list:
        return self.nodes[2:]

    def getEdgesNumber(self) -> int:
        return int(self.edgesNumber)

    def getEdgesBody(self) -> list:
        return self.edges[2:]

