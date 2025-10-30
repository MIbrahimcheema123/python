import random
import time
def getrandomdate(startdate,enddate):
    randomgenrater = random.random()
    dateformate ="%m/%d/%Y"
    starttime = time.mktime(time.strptime(startdate,dateformate))
    endtime = time.mktime(time.strptime(enddate,dateformate))
    randomtime = starttime+randomgenrater*(endtime-starttime)
    randomdate = time.strftime(dateformate,time.localtime(randomtime))
    return randomdate
print("randomdate is",getrandomdate("01/01/2000","04/09/2025"))