# Python3 code to demonstrate working of
# Convert day number to date in particular year
# Using datetime.strptime()
from datetime import datetime
  
# initializing day number
day_num = "339"
  
# print day number
print("The day number : " + str(day_num))
  
# adjusting day num
day_num.rjust(3 + len(day_num), '0')
  
# Initialize year
year = "2020"
  
# converting to date
res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%m-%d-%Y")
  
# printing result
print("Resolved date : " + str(res))