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
