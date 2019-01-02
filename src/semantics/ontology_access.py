'''
Created on 2 Jan 2019

@author: ejimenez-ruiz
'''
from owlready2 import *

class OntologyAccess(object):
    '''
    classdocs
    '''


    def __init__(self, pathontos, urionto):
        
        self.urionto = urionto
        
        #List from owlready2
        onto_path.append(pathontos) #For local ontologies
        
    
    
    def loadOntology(self, classify):   
        
        self.onto = get_ontology(self.urionto)
        self.onto.load()
        
        #self.classifiedOnto = get_ontology(self.urionto + '_classified')        
        if classify:
            with self.onto:
                sync_reasoner()  #it does add inferences to ontology
            
        #report problem with unsat (Nothing not declared....)
        #print(list(self.onto.inconsistent_classes()))
        
    
    
    def getOntology(self):
        return self.onto
    


folder_ontos="/home/ejimenez-ruiz/Documents/UK_BioBank/CMR-QA-ontology"
uri_onto="http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA"

onto_access = OntologyAccess(folder_ontos, uri_onto)
onto_access.loadOntology(True)

print(onto_access.getOntology().Cardiac_Cycle_Phase.iri)
print(onto_access.getOntology().Cardiac_Cycle_Phase.descendants())

descendants_str = set()
for cls in onto_access.getOntology().Cardiac_Cycle_Phase.descendants():
    descendants_str.add(cls.iri)

test_uri = "http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA#End-Diastole"
print(test_uri in onto_access.getOntology().Cardiac_Cycle_Phase.descendants())
print(descendants_str)
print(test_uri in descendants_str)



