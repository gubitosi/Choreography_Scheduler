from member import Member
import common

class Choreography:
	def __init__(self, choreographers, num_dancers = 0, difficulty = 1):
		if choreographers == None:
			self.choreographers = []
		else:
			self.choreographers = choreographers

		self.choreographers = num_dancers
		self.difficulty = difficulty
		self.availabilities = self.getOverlappingTimes()

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


	def getOverlappingTimes(self):
		if len(choreographers) == 0:
			return []
		availabities_calendar_df = choreographers[0].availabilities
		overlaps_df = generateBlankCalendar()
		for day in availabities_calendar_df:
			for time in availabities_calendar_df[day]:
				# check if each choreographer is present for the given day
				availability_slot = (day, time)
				if all(choreographer.availabilities[day][time] == 1 for choreographer in self.choreographers):
					overlaps_df[day][time] = 1

		return overlaps_df
