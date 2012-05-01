from datetime import datetime
from models.meeting import Meeting

class MeetingDAO:
    def all(self):
        return Meeting.all()

    def insert(self, meeting):
        Meeting.put(meeting)

    def next(self):
    	meetings = Meeting.all()
    	meetings.filter("day >=", datetime.now())
    	meetings.order("day")
    	return meetings.get()
