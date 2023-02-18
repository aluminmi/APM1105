#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Write a Python function to multiply all the numbers in a list.
def listMultiplier(listM):
    product = 1
    for x in listM:
        product = product * x
    return product

sampleList = [5, 6, -1, 2, 4, -2, -10, 7]
listMultiplier(sampleList)


# In[2]:


# Write a Python function to multiply all the numbers in a list. USER INPUT VERSION !
def listMultiplier(listM):
    product = 1
    for x in listM:
        product = product * x
    return product

sampleList = []

for i in range(8):
    sampleList.append(int(input('Input number; press enter to input the next number:')))

print("Your list is " + str(sampleList))
print("The product of your list is " + str(listMultiplier(sampleList)))


# In[36]:


# Write a function that draws a grid 
def rows():
    print("*", 4*'+', '♡', 4*'+', '⭑', 4*'-', '*', 4*'-', '♡')


def columns():
    for x in range(4):
        print('^', 4*' ', '$', 4*' ', '#', 4*' ', '✿', 4*' ','♪')


def grid():
    rows()
    columns()
    rows()
    columns()
    rows()
    columns()
    rows()
    columns()
    rows()
    columns()
    rows()
    columns()
    rows()
    


grid()


# In[ ]:




