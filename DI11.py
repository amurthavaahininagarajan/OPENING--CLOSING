#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


text_image = np.zeros((100,210),dtype = 'uint8')
font = cv2.FONT_HERSHEY_SIMPLEX = 3
cv2.putText(text_image,"Javith",(5,70),font,2,(255),5,cv2.LINE_AA)
plt.title("Original Image")
plt.imshow(text_image,'bone')
plt.axis('off')


# In[12]:


Kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11))


# In[14]:


opening_image = cv2.morphologyEx(text_image,cv2.MORPH_OPEN,Kernel)
plt.title("Opening")
plt.imshow(opening_image,'bone')
plt.axis('off')


# In[16]:


closing_image = cv2.morphologyEx(text_image,cv2.MORPH_CLOSE,Kernel)
plt.title("Closing")
plt.imshow(closing_image,'bone')
plt.axis('off')


# In[ ]:




