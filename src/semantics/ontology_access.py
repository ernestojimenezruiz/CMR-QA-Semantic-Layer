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
    
    
    #Does not seem to be a better way (or working way) according to the documentation...
    def getClassByURI(self, uri):
        
        for cls in list(self.getOntology().classes()):
            if (cls.iri==uri):
                return cls
            
        return None
            
    
    def getClassByName(self, name):
        
        for cls in list(self.getOntology().classes()):
            if (cls.name==name):
                return cls
            
        return None
    
    
    def getDescendantURIs(self,cls):
        descendants_str = set()
        
        for desc_cls in cls.descendants():
            descendants_str.add(desc_cls.iri)
        
        return descendants_str    
        
        
    def getDescendantNames(self,cls):
        descendants_str = set()
        
        for desc_cls in cls.descendants():
            descendants_str.add(desc_cls.name)
    
        return descendants_str
    
    
    
    def getDescendantNamesForClassName(self, cls_name):
        
        cls = self.getClassByName(cls_name)
        
        descendants_str = set()
        
        for desc_cls in cls.descendants():
            descendants_str.add(desc_cls.name)
    
        return descendants_str
        
        
    


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
print("Cardiac_Cycle_Phase" in onto_access.getOntology().Cardiac_Cycle_Phase.descendants())
print("Cardiac_Cycle_Phase" in onto_access.getOntology().Cardiac_Cycle_Phase.equivalent_to)
print(onto_access.getOntology().Cardiac_Cycle_Phaseqqqq)


print(onto_access.getClassByURI(test_uri))
print(onto_access.getClassByName("Cardiac_Cycle_Phase"))
print(onto_access.getClassByName("Cardiac_Cycle_Phase").descendants())
print(onto_access.getDescendantNames(onto_access.getClassByName("Cardiac_Cycle_Phase")))
print(onto_access.getDescendantURIs(onto_access.getClassByName("Cardiac_Cycle_Phase")))
print(onto_access.getDescendantNamesForClassName("Cardiac_Cycle_Phase"))
#print("Cardiac_Cycle_Phase" in onto_access.getOntology().Cardiac_Cycle_Phase.INDIRECT_equivalent_to)



