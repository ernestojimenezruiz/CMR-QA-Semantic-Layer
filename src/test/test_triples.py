'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''
from semantics.triple_generator import TripleGenerator
import pandas as pd
from csv_utils.csv_reader import CSVQAReader

file_csv = '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.csv'

#From excel to CSV
data_xls = pd.read_excel('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('file_csv', encoding='utf-8')
    

#qa_reader = CSVQAReader('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.csv')    
#csvreader=qa_reader.getCSVReader()


output_file = '/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.ttl'
TripleGenerator(file_csv, output_file)