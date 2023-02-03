#!/usr/bin/env python
# coding: utf-8

# In[17]:


# exercise 
km = float(input("Enter value in km:"))

miles = km/1.61
print("The kilometer in miles is:")
print(float(miles))


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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




