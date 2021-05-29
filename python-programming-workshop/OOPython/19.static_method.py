
class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def slash_to_dash(date):
        return date.replace("/", "-")


date = Dates("15-11-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.slash_to_dash(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
