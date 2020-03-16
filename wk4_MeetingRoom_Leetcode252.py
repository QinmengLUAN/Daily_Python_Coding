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



meeting_list = [MeetingTime(1, 2), MeetingTime(1, 6), MeetingTime(3, 4), MeetingTime(8, 1)]

print(AttendAll(meeting_list))

# print(meeting_list)

