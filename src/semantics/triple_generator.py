'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''
from csv_utils.csv_reader import CSVQAReader
from rdflib import graph, URIRef, BNode, Literal
from rdflib.namespace import RDF, RDFS, OWL


class TripleGenerator(object):
    '''
    Creates triples from CSV file according to CMR_QA ontology
    We use RDFlib: https://rdflib.readthedocs.io/en/stable/gettingstarted.html
    '''

    def __init__(self, csv_file_name):
        
        
        self.qa_reader = CSVQAReader(csv_file_name)    
        csvreader=self.qa_reader.getCSVReader()

        #Ignore first row
        next(csvreader)

        for row in csvreader:
            self.createTriples(row)
            
        
        self.qa_reader.closeFile()
        
        
    def createTriples(self, row_dict):
        
        #self.qa_reader.getRowID(row_dict)
        
        self.rdfgraph = graph()
        
        #Instances of http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA#Cine-MRI_Quality_Data
        
        #Examples
        #bob = URIRef("http://example.org/people/Bob")
        #linda = BNode() # a GUID is generated
        #name = Literal('Bob') # passing a string
        #age = Literal(24) # passing a python int
        #self.rdfgraph.add( (bob, RDF.type, FOAF.Person) )
        #self.rdfgraph.add( (linda, FOAF.name, Literal('Linda') ) )
        
        print(self.rdfgraph.serialize(format='turtle'))
        
        
        
        
        
        