# Exp11-Record-Implementation of Opening and Closing

## AIM:
To implement Opening and Closing using Python and OpenCV.

## SOFTWARE REQUIRED:
Anaconda - Python 3.7

OpenCV
## ALGORITHM:
### Step 1:
Import the necessary packages.

### Step 2:
Create the Text using cv2.putText.

### Step 3:
Create the structuring element.

### Step 4:
Use Opening operation.

### Step 5:
Use Closing Operation.

### Step 6:
Print the output and end the program.
## PROGRAM:
Developed by : Rama E. K. Lekshmi

Register number : 212222240082
### Import the necessary packages
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```
### Create the Text using cv2.putText
```python
text_image = np.zeros((100,190),dtype = 'uint8')
font = cv2.FONT_HERSHEY_SIMPLEX = 3
cv2.putText(text_image,"Javith",(5,70),font,2,(255),5,cv2.LINE_AA)
plt.title("Original Image")
plt.imshow(text_image,'magma')
plt.axis('off')
```
### Create the structuring element
```python
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
```

### Use Opening operation
```python
opening_image = cv2.morphologyEx(text_image,cv2.MORPH_OPEN,kernel)
plt.title("Opening")
plt.imshow(opening_image,'magma')
plt.axis('off')
```
### Use Closing Operation
```python
closing_image = cv2.morphologyEx(text_image,cv2.MORPH_CLOSE,kernel)
plt.title("Closing")
plt.imshow(closing_image,'magma')
plt.axis('off')
```

## OUTPUT:

### Input Image

![11](https://github.com/Rama-Lekshmi/OPENING--CLOSING/assets/118541549/ed235473-69d9-447d-871e-1e7d10aa376a)


### Result of Opening

![22](https://github.com/Rama-Lekshmi/OPENING--CLOSING/assets/118541549/2f25d905-65a5-4db6-8073-75bee057f02c)


### Result of Closing

![33](https://github.com/Rama-Lekshmi/OPENING--CLOSING/assets/118541549/1d1ebf93-26d4-4bdc-915b-d0ac3415710f)


## RESULT:
Thus, the Opening and Closing operation is used in the image using python and OpenCV.
