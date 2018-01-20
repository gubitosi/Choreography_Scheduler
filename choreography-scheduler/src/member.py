class Member:
    def __init__(self, 
                 name = None, danceRole = None, lRank = None, wRank = None,
                 availability = None, tCommit = None, pref = None):
        
        if name is None:
            name = "blah" + str(random.randrange(0,10))
        
        self.name = name
        
        if danceRole is None:
            danceRoles = ['L','F','B']
            danceRole = random.choice(danceRoles)
        
        self.danceRole = danceRole
        
        danceRanks = [1,2,3,4]
        if lRank is None:
            lRank = random.choice(danceRanks)
        if wRank is None:
            wRank = random.choice(danceRanks)
        
        self.lRank = lRank
        self.wRank = wRank
                
        if availability is None:
            availability = newWeeklyScheduleGenerator()
        
        self.availability = availability
        
        tCommits = [1,2,3,4,5,6,7]
        if tCommit is None:
            tCommit = random.choice(tCommits)
        
        self.tCommit = tCommit
        
        prefs = [['L','W'],['W','L']]
        if pref is None:
            pref = random.choice(prefs)
        
        self.pref = pref
