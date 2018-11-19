import csv

'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''


class CSVQAReader:


    def __init__(self, csv_file_name):
        self.openFile(csv_file_name)
        
        self.csvreader = csv.DictReader(
            self.csvfile, 
            fieldnames=['id', 'Scan_date', 'Patient_name', 'Patient_ID', 'Observer', 'Comment', 'LV', 'RV', 'LA', 'RA'])
        
    
    
    
    def openFile(self, csv_file_name):
        self.csvfile=open(csv_file_name)
        
    
    def closeFile(self):
        self.csvfile.close()
    
    
    def getCSVReader(self):
        return self.csvreader
    
        
    
    def getRowID(self, dict_scan):
        return dict_scan.get('id') 
    
         
    def getScanDate(self, dict_scan):
        return dict_scan.get('Scan_date') 
    
    def getPatienName(self, dict_scan):
        return dict_scan.get('Patient_name') 
    
    def getPatientID(self, dict_scan):
        return dict_scan.get('Patient_ID') 
    
    def getObserver(self, dict_scan):
        return dict_scan.get('Observer') 
    
    def getQAComment(self, dict_scan):
        return dict_scan.get('Comment') 
    
    
    
    ##Missing score == 1 (good quality)
    def getLVScore(self, dict_scan):
        if (dict_scan.get('LV')==''):
            return 1;
        return round(float(dict_scan.get('LV'))) 
    
    def getRVScore(self, dict_scan):
        if (dict_scan.get('RV')==''):
            return 1;
        return round(float(dict_scan.get('RV')))
    
    def getLAScore(self, dict_scan):
        if (dict_scan.get('LA')==''):
            return 1;
        return round(float(dict_scan.get('LA')))
    
    def getRAScore(self, dict_scan):
        if (dict_scan.get('RA')==''):
            return 1;
        return round(float(dict_scan.get('RA')))
    
    
    