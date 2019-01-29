import csv

'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''


class CSVQAReader:


    def __init__(self, csv_file_name, extended_annotation):
        self.openFile(csv_file_name)
        
        if extended_annotation: ##Including manual annotation
            fieldnames=['id', 'Patient_Name', 'Study_Date', 'Comment', 'LVQC', 'RVQC', 'LAQC', 'RAQC', 'Artefact', 'Motion_Artefact', 'Lack_Coverage', 'Image_Planning_Issue', 'Pathology', 'Triggering_Issue', 'Missing_Data', 'Poor_Quality', 'Unspecified_Issue', 'Score_Mismatch'] 
        else:
            fieldnames=['id', 'Patient_Name', 'Study_Date', 'Comment', 'LVQC', 'RVQC', 'LAQC', 'RAQC']
            ##fieldnames=['id', 'Scan_date', 'Patient_name', 'Patient_ID', 'Observer', 'Comment', 'LV', 'RV', 'LA', 'RA']
        
        self.csvreader = csv.DictReader(
            self.csvfile, 
            fieldnames)
    
    
    def openFile(self, csv_file_name):
        self.csvfile=open(csv_file_name)
        
    
    def closeFile(self):
        self.csvfile.close()
    
    
    def getCSVReader(self):
        return self.csvreader
    
        
    
    def getRowID(self, dict_scan):
        return dict_scan.get('id') 
    
         
    def getScanDate(self, dict_scan):
        return dict_scan.get('Study_Date') 
    
    def getPatienName(self, dict_scan):
        return dict_scan.get('Patient_Name') 
    
    def getPatientID(self, dict_scan):
        return dict_scan.get('Patient_ID') 
    
    def getObserver(self, dict_scan):
        return dict_scan.get('Observer') 
    
    def getQAComment(self, dict_scan):
        return dict_scan.get('Comment') 
    
    
    
    ##Missing score == 1 (good quality)
    def getLVScore(self, dict_scan):
        if (dict_scan.get('LVQC')==''):
            return 1;
        return round(float(dict_scan.get('LVQC'))) 
    
    def getRVScore(self, dict_scan):
        if (dict_scan.get('RVQC')==''):
            return 1;
        return round(float(dict_scan.get('RVQC')))
    
    def getLAScore(self, dict_scan):
        if (dict_scan.get('LAQC')==''):
            return 1;
        return round(float(dict_scan.get('LAQC')))
    
    def getRAScore(self, dict_scan):
        if (dict_scan.get('RAQC')==''):
            return 1;
        return round(float(dict_scan.get('RAQC')))
    
    
    def getLocationOfArtefact(self, dict_scan):
        return dict_scan.get('Artefact')
    
    def getLocationOfMotionArtefact(self, dict_scan):
        return dict_scan.get('Motion_Artefact') 
    
    def getLocationOfLackCoverage(self, dict_scan):
        return dict_scan.get('Lack_Coverage') 
    
    
    def getLocationOfImagePlanningIssue(self, dict_scan):
        return dict_scan.get('Image_Planning_Issue') 
    
    def getLocationOfPathology(self, dict_scan):
        return dict_scan.get('Pathology') 
    
    def getLocationOfTriggeringIssue(self, dict_scan):
        return dict_scan.get('Triggering_Issue') 
    
    def getLocationOfMissingData(self, dict_scan):
        return dict_scan.get('Missing_Data') 
    
    def getLocationOfPoorQuality(self, dict_scan):
        return dict_scan.get('Poor_Quality') 
    
    def getLocationOfUnspecifiedIssue(self, dict_scan):
        return dict_scan.get('Unspecified_Issue') 
    
    def getLocationOfScoreMismatch(self, dict_scan):
        return dict_scan.get('Score_Mismatch') 
    
    

    
    