import numpy as np
import pandas as pd


def generateBlankCalendar():
        newSchedule = pd.DataFrame(
        index = ['3:00','3:30','4:00','4:30','5:00','5:30','6:00','6:30','7:00','7:30',
                 '8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30'],
        columns=['M','Tu','W','Th','F','S','Su'],
        )

        #initialize all to 0
        for day in newSchedule:
            for time in newSchedule[day]:
                newSchedule[day][time] = 0
        
        return newSchedule
