import sys
from InitialFile import InitialFile
from Graph import Graph
from LPFile import LPFile

def startingScript():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        p = int(sys.argv[2])
        initialFile = InitialFile(filename, p)
        if initialFile.checkFormat():
            graph = Graph(initialFile)
            lpFile = LPFile(graph)
            lpFile.save()
        else:
            print("The format of the file is not correct")
            print("Please use the same format as the file ./instances/test.txt")
    else:
        print("No arguments provided")
        print("Please use the command with parameter like this:")
        print("lpconverter filename p")
        print("filename is the file that need to be convert")
        print("p can be of value 0 or 1, 0 mean aggregate model and 1 mean disaggregated model")
        exit(-1)


if __name__ == '__main__':
    startingScript()

