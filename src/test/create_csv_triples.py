'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''
from semantics.triple_generator import TripleGenerator
import pandas as pd
from csv_utils.csv_reader import CSVQAReader
from semantics.query_rdf_graph import QueryRDFGraph

file_csv = '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.csv'

#From excel to CSV
data_xls = pd.read_excel('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv(file_csv, encoding='utf-8')
    

#qa_reader = CSVQAReader('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.csv')    
#csvreader=qa_reader.getCSVReader()


#creates triples
output_file = '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.ttl'
TripleGenerator(file_csv, output_file)


#prepares comments
qManager = QueryRDFGraph(output_file)
qres = qManager.getQualityComments()


file = open("/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100_comments.txt", 'w') 
        
        
#Return qres and store in file: id|comment -> row[0]|row[1]
for row in qres:
    #print("%s has comment %s" % row)
    label=row[0].split("#")[1]
    comment=row[1].lower()
    #Minor fixes
    comment=comment.replace("&"," and ")
    comment=comment.replace("/"," and ")
    comment=comment.replace("$","4")
    comment=comment.replace("2 ","2ch ")
    comment=comment.replace("4 ","4ch ")
    comment=comment.replace("vol.","volume")
    comment=comment.replace("1 ","one ")
    comment=comment.replace("several","multiple")
    comment=comment.replace("some","few")
    print(label, comment)
    print(label + "|" + comment, file=file)
            
            
            


