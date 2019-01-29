'''
Created on 31 Oct 2018

@author: ejimenez-ruiz
'''
import json
from pprint import pprint


class JSONTKBGAnnotationReader(object):
    '''
    classdocs
    '''
   

    def __init__(self, file):
        '''
        Constructor
        '''
        #file='data.json'
        with open(file) as f:
            data = json.load(f)

        #pprint(data)
        #Accessing
        #data["maps"][0]["id"]
        #data["masks"]["id"]
        #data["om_points"]
        
        #pprint(data["Annotations"])
        for annotation in data["Annotations"]:
            print(annotation['cui'])
            print(annotation)


class JSONTKBGAnnotationAccess(object):
    
    #def __init__(self):
    
    def getCUI(self, json_annotation):
        return json_annotation['cui']
    
    
    def getPosition(self, json_annotation):
        return json_annotation['offset']
    
    
    def getSemType(self, json_annotation):
        return json_annotation['type']
    
    def getSemGroup(self, json_annotation):
        return json_annotation['grp']
    
    
    def getMatchedText(self, json_annotation):
        return json_annotation['match']
    
    def getLengthMatchedText(self, json_annotation):
        return json_annotation['len']
    
    
    




#JSONTKBGAnnotationReader("/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100Annotations/tkbgtagger/image_quality_data_2014_05_25_3275.json")      
#json_str='{"src": "cmr-qa", "score": 1, "len": 2, "grp": "CONC", "offset": 0, "idf": 4, "match": "la", "type": "ANAT", "id": "image_quality_data_2014_05_25_3275.e112", "cui": "Left_Atrium"}'
#tkbgaccess = JSONTKBGAnnotationAccess()
#print(tkbgaccess.getCUI(json.loads(json_str)))
#print(tkbgaccess.getPosition(json.loads(json_str)))
#print(tkbgaccess.getSemType(json.loads(json_str)))
#print(tkbgaccess.getSemGroup(json.loads(json_str)))
#print(tkbgaccess.getMatchedText(json.loads(json_str)))
#print(tkbgaccess.getLengthMatchedText(json.loads(json_str)))#


