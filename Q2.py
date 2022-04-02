class clockTime: #clockclass
    #initialize the time
    hour=0
    minute=0
    seconds=0


    def setHours(self, hour): #setter for hours
        self.hour=hour

    def setMinutes(self, minute):#setter for minute
        self.minute=minute

    def setSeconds(self, seconds):#setter for seconds
        self.seconds=seconds

    def setTime(self,hours,minutes,seconds):#setter for time
        self.hour=hours
        self.minute=minutes
        self.seconds=seconds

    def showTime(self):#method for showing current time
        time=str(self.hour) + ":" + str(self.minute) + ":" + str(self.seconds)
        return time

clock= clockTime() #instantiase clock object
hour=input("Please enter hour: ") #get user input
minute=input("Please enter minute: ")#get user input
second=input("Please enter second: ")#get user input
clock.setHours(hour) #set hours
clock.setMinutes(minute) #set minutes
clock.setSeconds(second) #set seconds
print("The time is " + clock.showTime()) #print out time