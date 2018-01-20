# NO TOUCHEY #

# Import stuff
import numpy as np
import pandas as pd
import random

test = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   '1mtrcZp-kpQWZ0X-lUrka1_3FAylbS2GBnSBBZG7vgmc' +
                   '/export?gid=1390846305&format=csv',
                   # Set first column as rownames in data frame
                   index_col=0,
                   # Parse column values to datetime
                   
                  )

test = test.dropna(axis=0)

test

testT = test.T
testT.columns.values[0] = "time"
testT.set_index('time', inplace=True)
testT

testT.replace({'free': 1}, regex=True)

# NO TOUCHEY #

# +: Generalize | Create array indices generator 

# Create mock schedule | Insert item 
# Input: (start_time,end_time,time_interval)
# Output: (newSchedule) one week of calendar

def newWeeklyScheduleGenerator():
    newSchedule = pd.DataFrame(
    index = ['3:00','3:30','4:00','4:30','5:00','5:30','6:00','6:30','7:00','7:30',
             '8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30'],
    columns=['M','Tu','W','Th','F','S','Su'],
    )
    return newSchedule


# NO TOUCHEY # 

# Generates a random schedule (used for testing)
# Input: (sd) template calendar
# Output: (rand_sd) filled random calendar of 1 or 0

def scheduleRandomizer(sd):
    rand_sd = pd.DataFrame(
        np.random.randint(0,2,size=(len(sd.index),len(sd.columns))),
        index=sd.index,
        columns=sd.columns)
    return rand_sd

# USE THIS #

def applySpaceAllocation(sd):
    sd.M['5:00':'10:00'] = 1
    sd.Tu['6:30':'9:00'] = 1
    sd.W['4:00':'8:00'] = 1
    sd.Th[:] = 0
    sd.F[:] = 0
    sd.S[:] = 1
    sd.Su['3:00':'11:30'] = 1
    sd.fillna(0,inplace=True)
    return sd

# NO TOUCHEY # 

# Member Class Declaration

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

# USE THIS #

# Troupe Member Declaration

# Leads 
albert = Member(name = "albert", danceRole = "L")
anthony = Member(name = "anthony", danceRole = "L")
bill = Member(name = "bill", danceRole = "L")
billy = Member(name = "billy", danceRole = "L")
brett = Member(name = "brett", danceRole = "L")
chetan = Member(name = "chetan", danceRole = "L")
colin = Member(name = "colin", danceRole = "L")
jacob = Member(name = "jacob", danceRole = "L")
joebert = Member(name = "joebert", danceRole = "L")
keri = Member(name = "keri", danceRole = "L")
kevin_a = Member(name = "kevin_a", danceRole = "L")
kevin_w = Member(name = "kevin_w", danceRole = "L")
nick = Member(name = "nick", danceRole = "L")
steven = Member(name = "steven", danceRole = "L")
trent = Member(name = "trent", danceRole = "L")
vincent = Member(name = "vincent", danceRole = "L")
walter = Member(name = "walter", danceRole = "L")
will =  Member(name = "will", danceRole = "L")

# Follows 
amy = Member(name = "amy", danceRole = "F")
abby = Member(name = "abby", danceRole = "F")
amanda = Member(name = "amanda", danceRole = "F")
amber = Member(name = "amber", danceRole = "F")
claire = Member(name = "claire", danceRole = "F")
erin = Member(name = "erin", danceRole = "F")
jaime = Member(name = "jaime", danceRole = "F")
judy = Member(name = "judy", danceRole = "F")
kanika = Member(name = "kanika", danceRole = "F")
katie = Member(name = "katie", danceRole = "F")
kristin = Member(name = "kristin", danceRole = "F")
madeline = Member(name = "madeline", danceRole = "F")
malia = Member(name = "malia", danceRole = "F")
mikaela = Member(name = "mikaela", danceRole = "F")
olivia = Member(name = "olivia", danceRole = "F")
rin = Member(name = "rin", danceRole = "F")
stefan = Member(name = "stefan", danceRole = "F")
summer = Member(name = "summer", danceRole = "F")
tasya = Member(name = "tasya", danceRole = "F")
yarden = Member(name = "yarden", danceRole = "F")


# USE THIS #

leads = [   albert, anthony, bill, billy, 
            brett, chetan, colin, jacob, 
            joebert, keri, kevin_a, kevin_w, nick, 
            steven, trent, vincent, walter, will]

follows = [ amy, abby, amanda, amber, 
            claire, erin, jaime, judy, 
            kanika, katie, kristin, madeline, 
            malia, mikaela, olivia, rin, 
            stefan, summer, tasya, yarden]
           
members = [ albert, anthony, bill, billy, 
            brett, chetan, colin, jacob, 
            joebert, keri, kevin_a, kevin_w, nick, 
            steven, trent, vincent, walter, will,
            amy, abby, amanda, amber, 
            claire, erin, jaime, judy, 
            kanika, katie, kristin, madeline, 
            malia, mikaela, olivia, rin, 
            stefan, summer, tasya, yarden]

bill.availability

# USE THIS # 

# Apply Schedules to members 
# Stretch: Excel or Google Sheets Converter

def applySchedule(sd):
#Ex.sd.M['begin_time':'end_time'] = 1

    sd.M['8:00':'10:00'] = 1
    sd.Tu['6:30':'9:00'] = 0
    sd.W['4:00':'8:00'] = 0
    sd.Th[:] = 0
    sd.F[:] = 0
    sd.S['3:30':'7:00'] = 1
    sd.Su['6:00':'11:30'] = 1
    sd.fillna(0,inplace=True)
    return sd

# USE THIS # 

# Apply Schedules to Members
# Example:
applySchedule(bill.availability)

#check to see if its right! 
bill.availability

# USE THIS 

# ex. ['choreographer1','choreographer2',timeBlock=2,style=L,difficulty=3]

choreoDetails = [
 ['abby','chetan'],
 ['amanda','nick'],
 ['amy','joebert'],
 ['erin','joebert'],
 ['jaime','nick'],
 ['judy','albert'],
 ['katie','anthony'],
 ['malia','kevin'],
 ['mikaela','kevin_w'],
 ['mikaela','olivia'],
 ['rin','nick']
]

# Create Full Availability Schedule

max_avail = newWeeklyScheduleGenerator()

for i in max_avail:
    max_avail.loc[max_avail[i].isnull(),[i]] = max_avail.loc[max_avail[i].isnull(),i].apply(lambda x: [])

for m in members:
    m.availability.replace([1],m.name,inplace=True)
    for i in m.availability:
        for j in range(len(m.availability[i])):
            if m.availability[i][j] != 0:
                max_avail[i][j].append(m.availability[i][j])

# Apply Space Limitations 

rawSchedule = newWeeklyScheduleGenerator()
spaceSchedule = applySpaceAllocation(rawSchedule)

for i in spaceSchedule:
    for j in range(len(m.availability[i])):
        if spaceSchedule[i][j] == 0:
            max_avail[i][j] = 0
            
max_avail

# Create Choreographer Availability Schedule

pair_avail = newWeeklyScheduleGenerator()

for i in pair_avail:
    pair_avail.loc[pair_avail[i].isnull(),[i]] = pair_avail.loc[pair_avail[i].isnull(),i].apply(lambda x: [])

for i in max_avail:
    for j in range(len(max_avail[i])):
        if type(max_avail[i][j]) == list:
            for pair in choreoDetails:
                if all(x in max_avail[i][j] for x in pair):
                    pair_avail[i][j].append(pair)
            
            # Warning if pair never matched
                    
pair_avail

# Adjust Choreography Availability for greater than 30 min blocks

hour_block_sched = newWeeklyScheduleGenerator()
filled = []

for i in pair_avail:
    hour_block_sched.loc[hour_block_sched[i].isnull(),[i]] = hour_block_sched.loc[hour_block_sched[i].isnull(),i].apply(lambda x: [])
    for j in range(len(pair_avail[i])):
        for pair in pair_avail[i][j]:
            if j == 0:
                if pair in pair_avail[i][j+1]:
                    hour_block_sched[i][j].append(pair)                    
            elif j == (len(pair_avail[i])-1): # for 11:30pm
                if pair in pair_avail[i][j-1]:
                    hour_block_sched[i][j].append(pair)
                #if len(test[i][j]) == 1:
                #    filled.append(pair)
                #else:
                #    for pairs in filled:
                #        test[i][j].remove(pairs)
                    
            else:
                if pair in pair_avail[i][j+1] or pair in pair_avail[i][j-1]:
                    hour_block_sched[i][j].append(pair)
        
hour_block_sched

# ScheduleReduce
# Input (schedule, pair)
# Output (reduced_schedule)

# Recursive along any time block

# If the block has only one pair
# check if other blocks with more than one pair have the same pair
# If yes | remove pair, else leave block alone
# If after removing block leaves only one pair, recall the function on the new block
# 

for i in test:
    test.loc[test[i].isnull(),[i]] = test.loc[test[i].isnull(),i].apply(lambda x: [])
    for j in range(len(pair_avail[i])):
        for pair in pair_avail[i][j]:

def avgScores(dancers,danceType):
    avgScore = 0
    if danceType == 'L':
        for dancer in dancers:
            avgScore += dancer.lRank    
    if danceType == 'W':
        for dancer in dancers:
            avgScore += dancer.wRank
    
    avgScore = avgScore / len(dancers)
    return avgScore
