'''
Created on 13 Aug 2019

@author: ejimenez-ruiz
'''

class QualityIssueGroup(object):
    '''
    This class will store information about a comment regarding a quality issue
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.issue="Unspecified_Issue" #default issue
        self.chambers=set()
        self.chamber_locations=set()
        self.views=set()
        self.cycle_phases=set()
        self.measures=set()
        self.modifiers=set() #important to define scores
        self.cardinality=""
        
        #Scores according the info in this group
        #1 is the default. No issue detected
        self.score_la=1
        self.score_ra=1
        self.score_lv=1
        self.score_rv=1
    
    
    def setIssue(self, qissue):
        self.issue = qissue
        
    def addChamber(self, chamber):
        self.chambers.add(chamber)
        
    def addChamberLocation(self, chamber_location):
        self.chamber_locations.add(chamber_location)
    
    def addView(self, view):
        self.views.add(view)
        
    def addCyclePhase(self, cycle):
        self.cycle_phases.add(cycle)
        
    def addMeasure(self, measure):
        self.measures.add(measure)
        
    def addModifier(self, modifier):
        self.modifiers.add(modifier)
        
    def setCardinality(self, card):
        self.cardinality=card
        
        
        
    def getIssue(self):
        return self.issue
        
    def getChambers(self):
        return self.chambers
        
    def getChamberLocations(self):
        return self.chamber_locations
    
    def getViews(self):
        return self.views
        
    def getCyclePhases(self):
        return self.cycle_phases
        
    def getMeasures(self):
        return self.measures
    
    def getModifiers(self):
        return self.modifiers
        
    def getCardinality(self):
        return self.cardinality
    
    
    
    def setScoreLA(self, score):
        self.score_la=score
    
    def setScoreRA(self, score):
        self.score_ra=score
        
    def setScoreLV(self, score):
        self.score_lv=score
        
    def setScoreRV(self, score):
        self.score_rv=score    
        
    
    def getScoreLA(self):
        return self.score_la
    
    def getScoreRA(self):
        return self.score_ra
    
    def getScoreLV(self):
        return self.score_lv
    
    def getScoreRV(self):
        return self.score_rv
    
    
    