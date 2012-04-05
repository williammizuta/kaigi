from models.meeting import Meeting

class MeetingDAO:
    def all(self):
        return Meeting.all()

    def insert(self, meeting):
        Meeting.put(meeting)
