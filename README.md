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
Developed by : Amurtha vaahini.KN

Register number : 212222240008
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

![111](https://github.com/amurthavaahininagarajan/OPENING--CLOSING/assets/118679102/ac20ab2b-ac0f-41a7-9209-099205022997)


### Result of Opening
![Screenshot 2023-11-07 203227](https://github.com/amurthavaahininagarajan/OPENING--CLOSING/assets/118679102/f8c9900a-b816-4665-9d28-333bfcf43cbf)




### Result of Closing

![Screenshot 2023-11-07 203305](https://github.com/amurthavaahininagarajan/OPENING--CLOSING/assets/118679102/0972f4d4-849f-4038-af79-b875679e4ca9)



## RESULT:
Thus, the Opening and Closing operation is used in the image using python and OpenCV.
