from Graph import Graph
class LPFile:
    def __init__(self, graph: Graph):
        self.graph = graph
    def save(self):
        constantDeclarationList = self.getConstantDeclaration()
        variableDeclarationList = self.getVariableDeclaration()
        optimalCondition = self.getoptimalCondition()
        conditionDeclarationList = self.getConditionDeclaration()
        filename = self.graph.file.split(".")[0]
        with open(".\LPFile\{filename}_{p}.lp".format(filename=self.graph.file.split(".")[0].split("\\")[1], p=self.graph.p), "w") as file:
            file.write(f"Minimize\n")
            file.write(f"   {optimalCondition}\n")
            file.write(f"Subject to\n")
            for declaration in conditionDeclarationList:
                file.write(f"   {declaration}\n")
            file.write(f"Bounds\n")
            for declaration in variableDeclarationList:
                file.write(f"   {declaration} >= 0\n")
            file.write(f"Integer\n")
            for declaration in variableDeclarationList:
                file.write(f"   {declaration}\n")
            file.write(f"End")





    def getConstantDeclaration(self):
        self.dictionnaire = dict()
        """
        pour tout les edges
        definir le cout pour chaque edge pour chaque produit
        """
        for i in range(self.graph.itemNumber):
            for edge in self.graph.edgeList:
                self.dictionnaire[f"const_e_{edge.start}_{edge.end}_{i}"] = edge.getCost(i)
        """
        pour tout source
        definir la capacite pour chaque produit
        """
        for i in range(self.graph.itemNumber):
            for source in self.graph.sourceList:
                self.dictionnaire[f"const_s_{source.id}_{i}"] = source.getCapacity(i)
        """
        pour tout destination,
        definir la demande pour chaque produit
        """
        for i in range(self.graph.itemNumber):
            for destination in self.graph.destinationList:
                self.dictionnaire[f"const_d_{destination.id}_{i}"] = destination.getDemand(i)
    def getVariableDeclaration(self) -> list:
        """
        declarer une variable pour la quantite passant sur une arrete pour chaque produit
        """
        temp = list()
        for i in range(self.graph.itemNumber):
            for edge in self.graph.edgeList:
                temp.append(f"quantity_e_{edge.start}_{edge.end}_{i}")
        return temp
    def getoptimalCondition(self) -> str:
        """
         pour TOut arete, somme des nombre de produit * cout du produit
        """
        temp = "z: "
        for i in range(self.graph.itemNumber):
            for edge in self.graph.edgeList:
                a = self.dictionnaire[f"const_e_{edge.start}_{edge.end}_{i}"]
                temp += f"{a} quantity_e_{edge.start}_{edge.end}_{i} + "
        temp = self.removingLastCharacter(temp) # removing the + added at the end
        return temp

    def getConditionDeclaration(self) -> list:

        temp = list()
        """
        pour chaque destination,
        la difference entre les produit entrant et les produit sortant doit etre egale a la demande
        """
        for i in range(self.graph.itemNumber):
            for destination in self.graph.destinationList:
                comingEdges = self.graph.getComingEdgeToNode(destination)
                exitingEdges = self.graph.getExitingEdgeToNode(destination)

                destination_add_list = []
                for comingEdge in comingEdges:
                    destination_add_list.append(f"quantity_e_{comingEdge.start}_{comingEdge.end}_{i}")

                destination_remove_list = []
                for exitingEdge in exitingEdges:
                    destination_remove_list.append(f"quantity_e_{exitingEdge.start}_{exitingEdge.end}_{i}")

                for remove in destination_remove_list:
                    if remove in destination_add_list:
                        destination_add_list.remove(remove)
                        destination_remove_list.remove(remove)

                comingEdgesSum = ""
                for add in destination_add_list:
                    comingEdgesSum += add + " + "
                comingEdgesSum = self.removingLastCharacter(comingEdgesSum)

                exitingEdgesSum = ""
                firstime = True
                for remove in destination_remove_list:
                    if firstime:
                        exitingEdgesSum += "- "
                        firstime = False
                    exitingEdgesSum += remove + " - "
                exitingEdgesSum = self.removingLastCharacter(exitingEdgesSum)

                temp.append("{contraite}: {sum1} {sum2} = {value}".format(contraite=f"contraite_{destination.id}_{i}", sum1=comingEdgesSum, sum2=exitingEdgesSum, value=self.dictionnaire[f"const_d_{destination.id}_{i}"]))

        """
        Pour tout source,
	    la difference entre les produits sortent et les produit entrant doit etre plus petit ou egal a la capacite
        """
        for i in range(self.graph.itemNumber):
            for source in self.graph.sourceList:
                comingEdges = self.graph.getComingEdgeToNode(source)
                exitingEdges = self.graph.getExitingEdgeToNode(source)

                destination_add_list = []
                for comingEdge in comingEdges:
                    destination_add_list.append(f"quantity_e_{comingEdge.start}_{comingEdge.end}_{i}")

                destination_remove_list = []
                firstime = True
                for exitingEdge in exitingEdges:
                    destination_remove_list.append(f"quantity_e_{exitingEdge.start}_{exitingEdge.end}_{i}")

                for remove in destination_remove_list:
                    if remove in destination_add_list:
                        destination_add_list.remove(remove)
                        destination_remove_list.remove(remove)

                comingEdgesSum = ""
                for add in destination_add_list:
                    if firstime:
                        comingEdgesSum += "- "
                        firstime = False
                    comingEdgesSum += add + " - "
                comingEdgesSum = self.removingLastCharacter(comingEdgesSum)

                exitingEdgesSum = ""
                for remove in destination_remove_list:
                    exitingEdgesSum += remove + " + "
                exitingEdgesSum = self.removingLastCharacter(exitingEdgesSum)

                temp.append("{contraite}: {sum1} {sum2} <= {value}".format(contraite=f"contraite_{source.id}_{i}", sum1=exitingEdgesSum, sum2=comingEdgesSum, value=self.dictionnaire[f"const_s_{source.id}_{i}"]))

        """
	    pour tout node qui n est pas source ni destination,
	    la somme des nombre de produit des arete entrant doit etre egal a la somme des nombre de produit des arete sortant
        """
        for i in range(self.graph.itemNumber):
            for node in self.graph.getNormalNode():
                comingEdges = self.graph.getComingEdgeToNode(node)
                exitingEdges = self.graph.getExitingEdgeToNode(node)

                destination_add_list = []
                for comingEdge in comingEdges:
                    destination_add_list.append(f"quantity_e_{comingEdge.start}_{comingEdge.end}_{i}")

                destination_remove_list = []
                for exitingEdge in exitingEdges:
                    destination_remove_list.append(f"quantity_e_{exitingEdge.start}_{exitingEdge.end}_{i}")

                for remove in destination_remove_list:
                    if remove in destination_add_list:
                        destination_add_list.remove(remove)
                        destination_remove_list.remove(remove)

                comingEdgesSum = ""
                for add in destination_add_list:
                    comingEdgesSum += add + " + "
                comingEdgesSum = self.removingLastCharacter(comingEdgesSum)

                exitingEdgesSum = ""
                firstime = True
                for remove in destination_remove_list:
                    if firstime:
                        exitingEdgesSum += "- "
                        firstime = False
                    exitingEdgesSum += remove + " - "
                exitingEdgesSum = self.removingLastCharacter(exitingEdgesSum)
                temp.append("{contraite}: {sum1} {sum2} = 0".format(contraite=f"contraite_{node.id}_{i}",
                                                                    sum1=comingEdgesSum,
                                                                    sum2=exitingEdgesSum))



        return temp
    def removingLastCharacter(self, string:str):
        return string[:-3]