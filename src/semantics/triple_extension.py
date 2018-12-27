'''
Created on 21 Nov 2018

@author: ejimenez-ruiz
'''
import rdflib
from rdflib.plugins.sparql import prepareQuery
from constants import CMR_QA
import json


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
        
        #It queries from current RDF grapg the quality data ids
        self.queryQualityDataIds()
        
        for row in self.qualityDataURIComments:
            self.processJSON4QualityComment(row[0], row[1], path_json_annotations)
            
        
    
    
    
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
        print(comment)
        for annotation in data["Annotations"]:
            print(annotation)
        
        
        #Group identified comments by offset. Groups will be defined by "." and ";", subcomments by ","
            
        
        
        
        
        
        
        
        
        
    

TripleExtension('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.ttl', '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100Annotations/tkbgtagger/')
        
        