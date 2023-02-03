#!/usr/bin/env python
# coding: utf-8


# In[17]:

# exercise 2
km = float(input("Enter value in km:"))

miles = km/1.61
print("The kilometer in miles is:")
print(float(miles))

# Exercise 3 answer 1
#There is 4.27 minutes in every km since 10km is equivalent to 42minutes and 42seconds
minutes_per_km = 4.27
km_per_mile = 1.61

km = int(input("Enter km: "))

miles = km / km_per_mile 
hours = minutes_per_km / 60
pace = minutes_per_km / miles
mph = miles / hours

print('The Pace/time in minutes per mile:', pace)
print('The Average speed in miles per hour:', mph)

#Exercise 3 answer 2
# In[27]:

km=float(input("Enter kilometer :"))
m = float(input("Enter minutes:"))
s = float(input("Enter seconds: "))

# km to mile
mile = km/1.61

# minutes to seconds
seconds = m * 60

# seconds to minutes

minutes = s / 60

#total minutes 
tm = (m+minutes) / mile

#total seconds 
ts = (s+seconds) / mile

# minutes to hours
mh = m / 60

#seconds to hours
sh = s / 3600

#total hours
th = mile / (mh +sh)

print("The average pace in seconds per mile is: ")
print("%.0f" %ts + " seconds per mile")
print("The average pace in minutes per mile is: ")
print("%.0f" %tm + " minutes per mile ")
print("The average pace in miles per hour is:")
print("%.0f" %tm + " miles per hour") 

