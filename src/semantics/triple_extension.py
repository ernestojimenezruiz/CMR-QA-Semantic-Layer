'''
Created on 21 Nov 2018

@author: ejimenez-ruiz
'''
import rdflib
from rdflib.plugins.sparql import prepareQuery
from constants import CMR_QA
import json
from annotations.annotation_reader import JSONTKBGAnnotationAccess
from owlready2 import *
from semantics.ontology_access import OntologyAccess

class TripleExtension(object):
    '''
    Creates (advanced) triples from quality comments according to CMR_QA ontology
    This class will extend the basic triples extracted from the CSV file
    with triples extracted from the comments. It will also extract the global 
    quality score and level 
    '''


    def __init__(self, file_rdf, path_json_annotations):
        '''
        Input: basic triples, json files from annotators. 
        Each file is named tool-quality_data_name.json
        For example: bioportal-image_quality_data_2014_06_25_7328.json
        or tkbgtagger-image_quality_data_2014_06_25_7328
        '''
        
        #The ones extracted directly from CSV file
        self.loadCurrentTriples(file_rdf)
        
        #It queries from current RDF graph the quality data ids
        self.queryQualityDataIds()
        
        #set upd ontology
        self.setUpOntology()
        
        i=1
        for row in self.qualityDataURIComments:
            print("Comments " + str(i))
            self.processJSON4QualityComment(row[0], row[1], path_json_annotations)
            i+=1
        
    
    
    def setUpOntology(self):
        folder_ontos="/home/ejimenez-ruiz/Documents/UK_BioBank/CMR-QA-ontology"
        uri_onto="http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA"

        self.onto_access = OntologyAccess(folder_ontos, uri_onto)
        self.onto_access.loadOntology(True)
    
    
    
       
    
    
    def loadCurrentTriples(self, file_rdf):
        
        self.rdfgraph = rdflib.Graph()
        self.rdfgraph.bind(CMR_QA.NAMESPACE_PREFIX, CMR_QA.BASE_URI)

        self.rdfgraph.parse(source=file_rdf, format='turtle')
        
    
    def queryQualityDataIds(self):
        
        query_str = """SELECT DISTINCT ?uri ?comment
           WHERE {
              ?uri """ + CMR_QA.NAMESPACE_PREFIX + """:"""+ CMR_QA.hasQualityComment_Name+ """ ?comment .
              ?uri rdf:type """ + CMR_QA.NAMESPACE_PREFIX + """:""" + CMR_QA.Cine_MRI_Quality_Data_Name + """ .
           }"""
        query_object = prepareQuery(query_str, initNs={CMR_QA.NAMESPACE_PREFIX : CMR_QA.BASE_URI})
           
        #print(query2)
    
        self.qualityDataURIComments = self.rdfgraph.query(query_object)
        
        
        
    def processJSON4QualityComment(self, quality_uri, comment, path_json_annotations):
        
        quality_name = quality_uri.split("#")[1]
        
        file = path_json_annotations + quality_name + '.json'
        with open(file) as f:
            data = json.load(f)
        
        print(quality_name)   
         
         
        #1. Group identified comments by offset. Groups will be defined by "." and ";", subcomments by ","
        #Characters to split different comments
        #We should split also by "," and then try to merge issues with previous one if for example issue is unspecified 
        #and what is mentioned is compatible, no more mentions of views or issues, but sth about affecting volumes
        #Merging issues may be wrt the comments before or after.
        
        
        chars=[".",";",","]
        
        positions_end_comment = ( [pos for pos, char in enumerate(comment) if char in chars])
        
        size_comment= len(comment)-1
        
        if size_comment not in positions_end_comment:
            positions_end_comment.append(size_comment) 
        
        print(comment, positions_end_comment)
            
        ##Initialize annotation groups 
        sem_annotations = {}        
        for i in range(len(positions_end_comment)):
            sem_annotations[i]=[]
            #print(str(i) + " - " + str(positions_end_comment[i]))
        
        tkbgAnnotationAccess = JSONTKBGAnnotationAccess()   
        
        for annotation in data["Annotations"]:
            #print(annotation)
            #print(tkbgAnnotationaccess.getCUI(annotation))
            position = tkbgAnnotationAccess.getPosition(annotation)
            for i in range(len(positions_end_comment)):
                if position <= positions_end_comment[i]:
                    sem_annotations[i].append(tkbgAnnotationAccess.getCUI(annotation))
                    break
         
         
        print(sem_annotations)
  
  
        ##TODO: We may need to complement annotations with dictionary look-up. ch4 is missing in some cases
        
        
        #2. Aswer questions: What (class issue), where (chamber, view, chamber location), when (cycle), how affects (measure), how many (cardinality), etc.
        #We ask for subclasses of relevant classes
        for key in sem_annotations:
            
            issue="Unspecified_Issue" #default issue
            chambers=set()
            chamber_locations=set()
            views=set()
            
            #Potential problems:
            #e.g. image_quality_data_20140822_5741|motion artefact, sv not matching, ?draw sax slice 2ch on systole, artefact in la on 4ch (needs review)
            # ?draw sax slice 2ch on systole -> two different views?
            
            for concept in sem_annotations.get(key):
                
                print(concept)
                
                if concept in self.onto_access.getDescendantNamesForClassName("Motion_Artefact"):
                    pass
                
                elif concept in self.onto_access.getDescendantNamesForClassName("Cardiac_Chamber"):
                    chambers.add(concept)
                elif concept in self.onto_access.getDescendantNamesForClassName("Chamber_Location"):
                    chamber_locations.add(concept)
                elif concept in self.onto_access.getDescendantNamesForClassName("Cardiac_Imaging_Plane"):
                    views.add(concept)
                
                
                
                
        
        
        #Preliminary evaluation: issue and chamber
        
        
        #When
        #onto_access.getOntology().Cardiac_Cycle_Phase.descendants()
        
        
        
                
         
        
        
        
        
        
        
        
        ##3. Apply rules by group of comments, only if not mentioned chamber for example. Otherwise we may bring ambiguity
        #HLA (4ch) -> LA or RA
        #VLA (2ch) -> LA 
        #SAX -> LV or RV
        
            
            
        
        
        
            
        #Apply patterns and build new triples
        
        #Then predict scores
        
        #To enhance the access to the annotations, the "type" could be more meaningful trying to answer to the 5-6 questions:
        #0. Issue (finding), 1. chamber (ANAT), 2. camber location (ANAT2?),  3. view (SPATIAL), 4. Affected measure (Clinial attribute), 5. Cardinality slices () and 6 cardiac cycle (temporal)
        
        #Giving a better type may be difficult... but we can exploit the ontology (e.g. subclasses of Image issue)
        #We coudl read definition of ontology and the populate according to the restrictions in a "semi"-automatic fashion
        #With OWLready may even be easy to find the links between issue and outcome meausres for example
        #For cardinality use custom elements
        
        #As above we are getting the basic information detected. With patterns we may get more. Apply patterns first? It may make 
        #sense or have several iterations.
        
        #Note that we will need to create instances for type of issue, etc. 
        
        #id of issue may be similar to id of quality study (to identify it better?)
        
        #Classify few and slice as cardinality with some sort of pattern?  
        
        #Answer with onto  about quality issue:
        #What (class issue), where (chamber and view), when (cycle), how (measure), how many (cardinality), etc.
        
        #Create generic instances for the dimensions of an issue? la, ra, hla? (in ontology or additionally as external data?)
        #Both modelling choices are acceptable. I.e. same la as generic chamber or specific chamber of specific patient. 
        #It depends if we want to say sth specific about the chamber, whcih doe snot seem to be the case. 
        #They seem to be generic elements we obtained from the countouring/visualization systems.
        #  
        #Chamber location also informative when missing slices
        
        
        
        
        
        
        
        
    

TripleExtension(
    '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/Batch1-100/FirstBatch100.ttl', 
    '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/Batch1-100/tkbgtagger/')
        
        