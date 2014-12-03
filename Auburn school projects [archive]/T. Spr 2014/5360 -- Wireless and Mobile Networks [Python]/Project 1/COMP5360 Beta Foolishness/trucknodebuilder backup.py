'''
Created on 13 March, 2014

@author: aew0024 Albert Wallace
'''
import os

class TruckNodeBuilder:


    def __init__(self, configFileName, expectedNodeNumber):
        self.configFileLineCount = 0
        self.modifyLineNumber = -1
        self.configFileContents = []
        self.targetConfigFile = configFileName
        self.nodeValueBeingChecked = ''
        self.actualNodeNumber = -1
        self.tuxMachineAssignment = -1
        self.portNumberUDP = -1
        self.initialXPosition = -1
        self.initialYPosition = -1
        self.thisStringShouldReadAsLinks = "Not yet set to the word L i n k s"
        self.listOfNeighborNodes = []
        self.configFileForNodes = None
        self.rawNodeParamArray = []
        self.validLineFound = False
        self.writeXPosition = -1
        self.writeYPosition = -1
        self.writeListOfNeighborNodes = []

        self.readFromConfigFile(expectedNodeNumber, True)
        
        
    def readFromConfigFile(self, expectedNodeNumber, doUpdateInternalState):
        print doUpdateInternalState
        try:
            #pathToConfigFile = os.path.join((os.path.dirname(__file__)), self.targetConfigFile)
            #self.configFileForNodes = open(pathToConfigFile, 'r')
            self.configFileForNodes = open(self.targetConfigFile, 'r')
            #must fix this to check for only A versus TA
            self.nodeValueBeingChecked = 'Node ' + str(expectedNodeNumber)
            print 'INFO: CFG.read: Scanning for ' + self.nodeValueBeingChecked
            self.configFileContents = []
            self.configFileLineCount = 0
            for line in self.configFileForNodes: #for each line of the file, we have to parse info in the format "Node 1 tux175, 10010 50 120 links 2"
                self.configFileLineCount = self.configFileLineCount + 1
                print 'DEBUG: CFG.read: line being analyzed...: ' + str(line)
                self.configFileContents.append(line) #add the line read-in to the virtual copy of the file
                #doUpdateInternalState == True and
                if (-1 != line.find(self.nodeValueBeingChecked)): #if we don't find that basic bit of info in the line, the line is not for me; see the 'else' on how to handle
                    self.validLineFound = True
                    print 'INFO: CFG.read: Successfully found node info on line number {0:2d}. Will process this line and continue!'.format(self.configFileLineCount)
                    inputline = line #copy the line to a new string
                    #self.configFileForNodes.close() #close the file
                    self.rawNodeParamArray = inputline.split() #split the entry into level and weights for level using the white space
                    safetyComparator = self.rawNodeParamArray[0]
                    print 'DEBUG: CFG.read: line being processed...? ' + inputline
                    if ("Node" != safetyComparator):
                        print 'WARNING: CFG.read: Unexpected mismatch while reading file; algorithm unstable--do not trust results!'
                    #now convert the string into separate parameters
                    else:
                        loopuntil = self.rawNodeParamArray.__len__()
                        currentPositionOfParameterScan = 0;
                        while (currentPositionOfParameterScan < loopuntil):
                            if (currentPositionOfParameterScan == 0):
                                safetyComparator = safetyComparator #just doing something to do something...
                                #...since the word "Node" isn't necessary
                            elif (currentPositionOfParameterScan == 1):
                                #the input should be the node number, duplicated
                                self.actualNodeNumber = self.rawNodeParamArray[currentPositionOfParameterScan]
                            elif (currentPositionOfParameterScan == 2):
                                self.tuxMachineAssignment = self.rawNodeParamArray[currentPositionOfParameterScan]
                            elif (currentPositionOfParameterScan == 3):
                                self.portNumberUDP = self.rawNodeParamArray[currentPositionOfParameterScan]
                            elif (currentPositionOfParameterScan == 4):
                                self.initialXPosition = self.rawNodeParamArray[currentPositionOfParameterScan]
                            elif (currentPositionOfParameterScan == 5):
                                self.initialYPosition = self.rawNodeParamArray[currentPositionOfParameterScan]
                            elif (currentPositionOfParameterScan == 6):
                                self.thisStringShouldReadAsLinks = self.rawNodeParamArray[currentPositionOfParameterScan]
                                if (loopuntil == currentPositionOfParameterScan + 1):
                                    print 'DEBUG: CFG.read: Maybe OK! No neighbors. DBGNFO: ' + str(self.rawNodeParamArray[0]) + str(self.rawNodeParamArray[1]) + str(self.rawNodeParamArray[2]) + str(self.rawNodeParamArray[3])
                                else:
                                    print 'DEBUG: CFG.read: almost there during initial scan...'
                            elif (currentPositionOfParameterScan == 7):
                                self.listOfNeighborNodes = self.rawNodeParamArray[7:loopuntil]
                                    
                            currentPositionOfParameterScan = currentPositionOfParameterScan + 1
    
                else:
                    #display that the info was bad and we couldn't read that line
                    if (doUpdateInternalState == True):
                    	print 'DEBUG: CFG.read: Node info not found on line number {0:2d}. Continuing with next line, if available.'.format(self.configFileLineCount)
                    else:
                    	print 'INFO: CFG.read: Internal state variables left unchanged, but configuration file stored in memory.'
            #if the file was somehow opened but nothing was read in...
            if (self.validLineFound == True):
                print 'DEBUG: CFG.read: All OK! 1+ neighbors. '+ str(self.listOfNeighborNodes) + ' DBGNFO: ' + str(self.rawNodeParamArray[0]) + str(self.rawNodeParamArray[1]) + str(self.rawNodeParamArray[2]) + str(self.rawNodeParamArray[3])
                self.configFileForNodes.close() #close the file
                return self.rawNodeParamArray
            else:
                print 'ERROR: CFG.read: Assume no valid configuration info found in selected file.'
                self.configFileForNodes.close() #close the file
                return ['0']
                
        except IOError:
            print 'ERROR: CFG.read: Cannot open configuration file ' + self.targetConfigFile + '. Cannot successfully build or rebuild node in memory.'
            return ['-3']
	
    #used to update the three config file parameters that will be modified: X position, Y position, and neighbor nodes
    def updatePosition(self, Xcoord, Ycoord, neighborsList):
        self.writeXPosition = Xcoord
        self.writeYPosition = Ycoord
        tempListOfNeighborNodes = []
        tempListOfNeighborNodes.extend(neighborsList)
        self.writeListOfNeighborNodes = tempListOfNeighborNodes
	
    #We have to write out the new configuration information for a given node ONLY; do not update anything else for any other node.
    #So we write out the X and the Y information and maybe the nearest neighbors.
    def writeToConfigFile(self):
        stringRepresentationOfFile = str('\n\n')
        try:
            self.configFileForNodes = open(self.targetConfigFile, 'a')
            writeLineNumber = 0
            while (writeLineNumber < self.configFileLineCount):
              if (-1 != self.configFileContents[writeLineNumber].find(self.nodeValueBeingChecked)): #if this is the line that corresponds with this node, edit it
                modifiedStringOut = self.nodeValueBeingChecked + ' ' + self.tuxMachineAssignment + ' ' + str(self.portNumberUDP) + ' ' + str(self.writeXPosition) + ' ' + str(self.writeYPosition) + ' ' + self.thisStringShouldReadAsLinks + ' '
                for nodeNumber in self.writeListOfNeighborNodes:
                    modifiedStringOut += str(nodeNumber) + ' '
                modifiedStringOut += '\n'
                print 'DEBUG: CFG.writeUpdate: printing:::' + modifiedStringOut
                stringRepresentationOfFile += modifiedStringOut
                writeLineNumber = writeLineNumber + 1
              else: #print it back out without editing anything, as the line corresponds to another node
                  print 'DEBUG: CFG.writeBack: printing|||' + str(self.configFileContents[writeLineNumber])
                  stringRepresentationOfFile += str(self.configFileContents[writeLineNumber])
                  writeLineNumber = writeLineNumber + 1
            print stringRepresentationOfFile
            self.configFileForNodes.write(str(stringRepresentationOfFile))
            self.configFileForNodes.close()
        except IOError:
            print 'ERROR: CFG.write: Cannot open configuration file ' + self.targetConfigFile + '. Cannot successfully save current node status to storage.'

    def writeToImagingFile(self, imageFilePath):
        try:
            virtualImageFile = open(imageFilePath, 'a')

            virtualImageFile.close()
        except IOError:
            print 'ERROR: writeImgF: Cannot create/open imaging file ' + imageFilePath + '. Cannot successfully save visualization.'
