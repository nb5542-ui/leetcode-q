class MyCalendar(object):

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime, endTime):
        for old_start,old_end in self.bookings:
            if startTime < old_end and endTime > old_start:
                return False

        self.bookings.append((startTime,endTime))

        return True
        

        

            
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)