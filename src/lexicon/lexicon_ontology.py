from owlready2 import *
from traitlets.config.application import catch_config_error
#import lexicon


#Class to extract the lexicon from the ontology annotations
class ExtractLexiconOntology:

    #Variable here shared by all instances
    
    
    def __init__(self, pathontos, urionto):
        
        self.urionto = urionto
        
        #Entries with key=name class and values the list of labels
        self.lexicon = {} # or with dict()
        #Entries with key=name class and values the list of semantic groups
        self.semGroups = {}
        
        #List from owlready2
        onto_path.append(pathontos) #For local ontologies
      
      
    def loadOntology(self):   
        
        self.onto = get_ontology(self.urionto)
        self.onto.load()
        
        #self.classifiedOnto = get_ontology(self.urionto + '_classified')        
        with self.onto:
            sync_reasoner()  #it does add inferences to ontology
            
        #report problem with unsat (Nothing not declared....)
        #print(list(self.onto.inconsistent_classes()))
        
        
        for cls in list(self.onto.classes()):
         
            self.lexicon[cls.name]=set()
            self.semGroups[cls.name]=set()
            
            print(cls.name)
            
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
            print(self.lexicon[cls.name])
            
            
            #Add semantic groups from itself and parents 
            #(equivalent classes, including self class, also in ancestors)
            for anc in cls.ancestors():
                try:
                    self.semGroups[cls.name].update(anc.semanticGroup)
                except AttributeError:
                    pass
            
            print(self.semGroups[cls.name])
            
            #print(cls.iri)
            #print(cls.ancestors())
            #print(cls.descendants())
            #print(cls.equivalent_to)
            
            print(cls.label)
            print('Preferred label')
            
            try:
                print(cls.prefLabel)
            except AttributeError:
                pass
                
            print('Alt labels')
            print(cls.altLabel)
            print('Short labels')
            print(cls.shortLabel)
            
            #We need to propagate from parents classes 
            print('Sem group')
            print(cls.semanticGroup)
            print('Sem type')
            print(cls.semanticType)
            print('Sem type id')
            print(cls.semanticTypeID)
            #semanticGroup
            #semanticType
            #semanticTypeID
            
            
        
        
        
        
        
        