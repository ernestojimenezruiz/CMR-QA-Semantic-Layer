'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''
import pandas as pd
from csv_utils.csv_reader import CSVQAReader

#From excel to CSV
data_xls = pd.read_excel('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.csv', encoding='utf-8')
    

qa_reader = CSVQAReader('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.csv')    
csvreader=qa_reader.getCSVReader()

#Ignore first row
next(csvreader)
#print("aaa",next(csvreader))

for row in csvreader:
    #print(row)
    print(qa_reader.getScanDate(row), qa_reader.getPatienName(row), 
          qa_reader.getPatientID(row), qa_reader.getObserver(row),
          qa_reader.getQAComment(row), qa_reader.getLVScore(row),
          qa_reader.getRVScore(row), qa_reader.getLAScore(row),
          qa_reader.getRAScore(row))

qa_reader.closeFile()