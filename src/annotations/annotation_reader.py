'''
Created on 31 Oct 2018

@author: ejimenez-ruiz
'''
import json
from pprint import pprint


class JSONTKBGAnnotation(object):
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

        pprint(data)
        #Accessing
        #data["maps"][0]["id"]
        #data["masks"]["id"]
        #data["om_points"]
        
        #pprint(data["Annotations"])
        for annotation in data["Annotations"]:
            print(annotation)
        
        


JSONTKBGAnnotation("/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100Annotations/tkbgtagger/image_quality_data_2014_04_30_5290.json")      


