# Use sort to solve problem
# Check wthether you can attend all meetings today

class MeetingTime:
	def __init__(self, start, finish):
		self.start = start
		self.finish = finish
	def GetStart(self):
		return self.start
	def GetFinish(self):
		return self.finish

	def __repr__(self):
		return str(self.start) + " " + str(self.finish) 

def AttendAll(meeting_list):
	meeting_list.sort(key = MeetingTime.GetStart)
	# print(len(meeting_list))
	# print(meeting_list[0].finish)

	for i in range(1, len(meeting_list)):
		if meeting_list[i].start < meeting_list[i - 1].finish:
			return False
	return True

def MeetingRoom(MeetingRoom):
	meeting_list.sort(key = MeetingTime.GetStart)

	conflict = 0
	max_conflict = 0
	room = 0

	i = 0 # Before 
	j = 1 # Current
	while j < len(meeting_list):

		while i < j and j < len(meeting_list):
			if meeting_list[j].start < meeting_list[i].finish:
				conflict += 1
				max_conflict = max(max_conflict, conflict)
				j += 1
			else:
				i += 1
				conflict = 0
		j += 1
	
	room = max_conflict + 1
	
	print(room)

	return room


meeting_list = [MeetingTime(1, 2), MeetingTime(1, 6), MeetingTime(3, 4), MeetingTime(3, 9)]

print(AttendAll(meeting_list))

MeetingRoom(meeting_list)