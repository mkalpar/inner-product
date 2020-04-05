#!/usr/bin/env python
# coding: utf-8

# In[17]:
# Merve Kalpar
# hw3 - q3

def innerProduct(v1,v2):
    sum = 0
    if len(v1) == len(v2):
        for i in range(0,len(v1)): #iterates through the elements in the lists
            sum = sum + v1[i]*v2[i] #the i-th elements of both vectors get multiplied, and added to the sum variable in each loop
        print('<v1,v2> = ',sum)
    else:
        print('Vectors needs to be of the same size for inner product!')


# In[19]:


#input lists as parameters which consists of the elements of the vectors
#in this example, it's two vectors with n = 5 elements
#can be changed to any n as long as both have the same length n
innerProduct([8,1,6,4,5],[1,2,3,4,5]) 

