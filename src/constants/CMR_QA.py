'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''
import random
from rdflib import URIRef

BASE_URI = "http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA#"

NAMESPACE_PREFIX = "cmrqa"


#Classes
Cine_MRI_Quality_Data = URIRef(BASE_URI + "Cine-MRI_Quality_Data")
Imaging_Scan_Visit = URIRef(BASE_URI + "Imaging_Scan_Visit")
Observer = URIRef(BASE_URI + "Observer")
Image_Quality_Issue = URIRef(BASE_URI + "Image_Quality_Issue")


#Object properties
hasQualityData = URIRef(BASE_URI + "hasQualityData")
hasObserver = URIRef(BASE_URI + "hasObserver")
hasImageIssue = URIRef(BASE_URI + "hasImageIssue")


#Data properties
scanDate = URIRef(BASE_URI + "scanDate")
participantId = URIRef(BASE_URI + "participantId")
observerId = URIRef(BASE_URI + "observerId")

#General scores (to be calculated)
hasQualityScore = URIRef(BASE_URI + "hasQualityScore")
hasQualityLevel = URIRef(BASE_URI + "hasQualityLevel")
#values from limited set
Discarded_Quality_Level = "Discarded"
Optimal_Quality_Level = "Optimal"
Suboptimal_Quality_Level = "Sub-optimal"



##Free text comment given
hasQualityComment = URIRef(BASE_URI + "hasQualityComment")

#Numerical scores given
hasLAQualityScore = URIRef(BASE_URI + "hasLAQualityScore")
hasRAQualityScore = URIRef(BASE_URI + "hasRAQualityScore")
hasLVQualityScore = URIRef(BASE_URI + "hasLVQualityScore")
hasRVQualityScore = URIRef(BASE_URI + "hasRVQualityScore")


observerBackground = URIRef(BASE_URI + "observerBackground") #values from limited set
Clinical_Observer_Background = "Clinical"
Analyst_Observer_Background = "Image Analyst"

observerExperience = URIRef(BASE_URI + "observerExperience") #values from limited set
Early_Training_Observer_Experience = "Early Training"
Experienced_Observer_Experience = "Experienced"
Supervisor_Observer_Experience = "Supervisor"



##Instances
vc = URIRef(BASE_URI + "vc")
el = URIRef(BASE_URI + "el")
na = URIRef(BASE_URI + "na")
ze = URIRef(BASE_URI + "ze")
mms = URIRef(BASE_URI + "mms")
kf = URIRef(BASE_URI + "kf")
yj = URIRef(BASE_URI + "yj")



def getObserverURI(ob_id):
    
    if ob_id=='':
        return na #observer
    
    return URIRef(BASE_URI + ob_id)


def createScanVisitResourceURI(date, rowid):
    return URIRef(BASE_URI + "scan_visit_" + date + "_" + rowid + "_" + str(random.randint(1,10000)))


def createQualityDataResourceURI(date):
    return URIRef(BASE_URI + "image_quality_data_" + date + "_" + str(random.randint(1,10000)))

def createQualityIssueResourceURI(size_comment):
    return URIRef(BASE_URI + "image_quality_issue_" + str(size_comment) + "_" + str(random.randint(1,10000)))






