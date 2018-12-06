'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''
from csv_utils.csv_reader import CSVQAReader
from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import RDF, RDFS, OWL
from constants import CMR_QA

class TripleGenerator(object):
    '''
    Creates (basic) triples from CSV file according to CMR_QA ontology
    We use RDFlib: https://rdflib.readthedocs.io/en/stable/gettingstarted.html
    '''

    def __init__(self, csv_file_name, output_file):
        
        
        self.qa_reader = CSVQAReader(csv_file_name)    
        csvreader=self.qa_reader.getCSVReader()

        #Ignore first row
        next(csvreader)
        
        self.rdfgraph = Graph()
        
        self.rdfgraph.bind(CMR_QA.NAMESPACE_PREFIX, CMR_QA.BASE_URI)

        for row in csvreader:
            self.createTriples(row)
            
        
        self.rdfgraph.serialize(output_file, format='turtle')
        self.qa_reader.closeFile()
        
        
    def createTriples(self, row_dict):
        
        #Instances of http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA#Cine-MRI_Quality_Data
        #CMR_QA.Cine_MRI_Quality_Data
        
        
        ##We need to create new URI for each:
        #imaging scan visit
        #quality data
        #observer: can we have an additional table? 
        
        row_id = self.qa_reader.getRowID(row_dict)
        scan_date = self.qa_reader.getScanDate(row_dict).replace("'", "_")
        participant_id = self.qa_reader.getPatientID(row_dict) + "-" + self.qa_reader.getPatienName(row_dict)
        ob_id = str(self.qa_reader.getObserver(row_dict)).lower()        
        comment = self.qa_reader.getQAComment(row_dict)
        
        scan_visit_uri = CMR_QA.createScanVisitResourceURI(scan_date, row_id)
        quality_data_uri = CMR_QA.createQualityDataResourceURI(scan_date)
        image_issue_uri = CMR_QA.createQualityIssueResourceURI(len(comment))
        
        ##Triples scan visit 
        self.rdfgraph.add( (scan_visit_uri, RDF.type, CMR_QA.Imaging_Scan_Visit) )
        self.rdfgraph.add( (scan_visit_uri, CMR_QA.participantId, Literal(participant_id)) )
        self.rdfgraph.add( (scan_visit_uri, CMR_QA.hasQualityData, quality_data_uri) )
        
        #Triples quality data
        self.rdfgraph.add( (quality_data_uri, RDF.type, CMR_QA.Cine_MRI_Quality_Data) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasObserver, CMR_QA.getObserverURI(ob_id)) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasQualityComment, Literal(comment)) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasLVQualityScore, Literal(self.qa_reader.getLVScore(row_dict))) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasRVQualityScore, Literal(self.qa_reader.getRVScore(row_dict))) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasLAQualityScore, Literal(self.qa_reader.getLAScore(row_dict))) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasRAQualityScore, Literal(self.qa_reader.getRAScore(row_dict))) )
        
        #Triples to be inferred
        #1. Issues in comment
        #2. Global score and quality level according to subscores and comment
        #self.rdfgraph.add( (quality_data_uri, CMR_QA.hasQualityLevel, Literal()) )
        #self.rdfgraph.add( (quality_data_uri, CMR_QA.hasRAQualityScore, Literal()) )
        self.rdfgraph.add( (quality_data_uri, CMR_QA.hasImageIssue, image_issue_uri) )
        
        ##Generate json file for annotations?
        ##It can be another process.... given URI quality data and comment
        ##We can later insert new triples and extend the graph
        
    
    
        
        