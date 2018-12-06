'''
Created on 22 Nov 2018

@author: ejimenez-ruiz
'''
import rdflib
from rdflib.plugins.sparql import prepareQuery
from constants import CMR_QA

class QueryRDFGraph(object):
    '''
    classdocs
    '''


    def __init__(self, file_rdf):
        '''
        Constructor
        '''
        
        self.rdfgraph = rdflib.Graph()
        self.rdfgraph.bind(CMR_QA.NAMESPACE_PREFIX, CMR_QA.BASE_URI)

        self.rdfgraph.parse(source=file_rdf, format='turtle')


    
    '''
    Returns dictionary URI_quality_data : quality_comment
    '''
    def getQualityComments(self):
    
        #query = """SELECT DISTINCT ?uri ?comment
        #   WHERE {
        #      ?uri <""" + CMR_QA.hasQualityComment +  """> ?comment .
        #      ?uri rdf:type <""" + CMR_QA.Cine_MRI_Quality_Data + """> .
        #   }"""
           
        query_str = """SELECT DISTINCT ?uri ?comment
           WHERE {
              ?uri """ + CMR_QA.NAMESPACE_PREFIX + """:"""+ CMR_QA.hasQualityComment_Name+ """ ?comment .
              ?uri rdf:type """ + CMR_QA.NAMESPACE_PREFIX + """:""" + CMR_QA.Cine_MRI_Quality_Data_Name + """ .
           }"""
        query_object = prepareQuery(query_str, initNs={CMR_QA.NAMESPACE_PREFIX : CMR_QA.BASE_URI})
           
        #print(query2)
    
        qres = self.rdfgraph.query(query_object)
        
        
        #Return qres and store in file: id|comment -> row[0]|row[1]
        for row in qres:
            #print("%s has comment %s" % row)
            print(row[0], row[1])
            
