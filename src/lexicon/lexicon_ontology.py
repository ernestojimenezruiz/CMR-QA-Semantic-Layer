from owlready2 import *
from semantics.ontology_access import OntologyAccess


#Class to extract the lexicon from the ontology annotations
class ExtractLexiconOntology:

    #Variable here shared by all instances
    
    
    def __init__(self, pathontos, urionto):
        
        #Entries with key=name class and values the list of labels
        self.lexicon = {} # or with dict()
        #Entries with key=name class and values the list of semantic groups
        self.semGroups = {}
        
        #oads ontology
        self.onto_access = OntologyAccess(pathontos, urionto)
        self.onto_access.loadOntology(True)        
    
    
    def getLexiconForClasses(self):
        return self.lexicon
    
    
    def getSemGroupsForClasses(self):
        return self.semGroups
      
    
        
    def extractLexicon(self):
            
        #for cls in list(self.onto.classes()):
        for cls in list(self.onto_access.getOntology().classes()):
         
            self.lexicon[cls.name]=set()
            self.semGroups[cls.name]=set()
            
            #print(cls.name)
            
            #self.lexicon[cls.name] = self.lexicon[cls.name] | set(cls.label)
            self.lexicon[cls.name].update(cls.label)
            
            
            
            #They may not be defined by default
            #Skos preferred label
            try:
                self.lexicon[cls.name].update(cls.prefLabel)
            except AttributeError:
                pass
                
            #Skos alternative label    
            try:
                self.lexicon[cls.name].update(cls.altLabel)
            except AttributeError:
                pass
            
            #Custom short annotation property
            try:
                self.lexicon[cls.name].update(cls.shortLabel)
            except AttributeError:
                pass
            
            
            #expand synonyms with parent ones or with rules?
            #off-axis in RV (or in certain view) -> RV off-axis
            #print(self.lexicon[cls.name])
            
            
            #Add semantic groups from itself and parents 
            #(equivalent classes, including self class, also in ancestors)
            for anc in cls.ancestors():
                try:
                    self.semGroups[cls.name].update(anc.semanticGroup)
                except AttributeError:
                    pass
            
            #print(self.semGroups[cls.name])
            
            #print(cls.iri)
            #print(cls.ancestors())
            #print(cls.descendants())
            #print(cls.equivalent_to)
            #print('Sem group')
            #print(cls.semanticGroup)
            #print('Sem type')
            #print(cls.semanticType)
            #print('Sem type id')
            #print(cls.semanticTypeID)
            
            
        
        
        
        
        
        