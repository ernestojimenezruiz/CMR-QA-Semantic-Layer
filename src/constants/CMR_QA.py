'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
'''

BASE_URI = "http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA#"


#Classes
Cine_MRI_Quality_Data = BASE_URI + "Cine-MRI_Quality_Data"
Imaging_Scan_Visit = BASE_URI + "Imaging_Scan_Visit"
Observer = BASE_URI + "Observer"
Image_Quality_Issue = BASE_URI + "Image_Quality_Issue"


#Object properties
hasQualityData = BASE_URI + "hasQualityData"
hasObserver = BASE_URI + "hasObserver"


#Data properties
scanDate = BASE_URI + "scanDate"
participantId = BASE_URI + "participantId"
observerId = BASE_URI + "observerId"

#General scores (to be calculated)
hasQualityScore = BASE_URI + "hasQualityScore"
hasQualityLevel = BASE_URI + "hasQualityLevel" 
#values from limited set
Discarded_Quality_Level = "Discarded"
Optimal_Quality_Level = "Optimal"
Suboptimal_Quality_Level = "Sub-optimal"



##Free text comment given
hasQualityComment = BASE_URI + "hasQualityComment"

#Numerical scores given
hasLAQualityScore = BASE_URI + "hasLAQualityScore"
hasRAQualityScore = BASE_URI + "hasRAQualityScore"
hasLVQualityScore = BASE_URI + "hasLVQualityScore"
hasRVQualityScore = BASE_URI + "hasRVQualityScore"


observerBackground = BASE_URI + "observerBackground" #values from limited set
Clinical_Observer_Background = "Clinical"
Analyst_Observer_Background = "Image Analyst"

observerExperience = BASE_URI + "" #values from limited set
Early_Training_Observer_Experience = "Early Training"
Experienced_Observer_Experience = "Experienced"
Supervisor_Observer_Experience = "Supervisor"



##Instances
vc = BASE_URI + "vc"
el = BASE_URI + "el"
na = BASE_URI + "na"
ze = BASE_URI + "ze"
mms = BASE_URI + "mms"
kf = BASE_URI + "kf"
yj = BASE_URI + "yj"



def getObserverURI(id):
    return BASE_URI + id 





