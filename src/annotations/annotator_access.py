'''
Created on 31 Oct 2018

@author: ejimenez-ruiz
'''
import requests
import json
import re,sys
import multiprocessing as mp
import gzip 


#class LocalTKBGAnnotator(object):   
#    def __init__(self):
        
        
    

class RemoteAnnotator(object):
    '''
    classdocs
    '''
    ##http://docs.python-requests.org/en/latest/user/quickstart/
    
    ##url = "https://krono.act.uji.es/annotator/cmr-qa/"
    ##Or BioPortal


    def __init__(self, url, query_text):
        '''
        Constructor
        '''
        response = requests.get(url, params=query_text)
        
        #print(response.url)
        if response.ok:
            print(response.json)
        else:
            # If response code is not ok (200), print the resulting http error code with description
            #response.raise_for_status()
            print("Error accesing: "+ str(response.url) + ". Status: " + str(response.status_code))
        
        

