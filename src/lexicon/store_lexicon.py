import os
import sys
#Example
#LA_off_axis:SPAT|LA off axis
#LA_off_axis:SPAT|Left Atrium off axis
#LA_off_axis:SPAT|L Atrium off axis
#Left_Atrium:ANAT|Left Atrium
#Left_Atrium:ANAT|LA
class StoreLexiconOntology:

    #Variable here shared by all instances
    
    def __init__(self, lexicon, semGroups, fileLex):
        
        absFilePath = os.path.abspath(__file__)
        fileDir = os.path.dirname(absFilePath)#module
        parentDir = os.path.dirname(fileDir)#src folder
        ROOT_DIR = os.path.dirname(parentDir)
    
        file = open(ROOT_DIR + '/lexicon/' + fileLex, 'w') 
     
        
        for cls in lexicon.keys():
            for label in lexicon[cls]:
                print(cls + ':' + next(iter(semGroups[cls])) + "|" + label) 
                print(cls + ':' + next(iter(semGroups[cls])) + "|" + label, file=file)
