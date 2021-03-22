import streamlit as st
from PIL import Image
import numpy as np
import cv2
import random



DEMO_IMAGE = 'sample.jpg'

#color1 = (list(np.random.choice(range(256), size=3)))  
#color =[int(color1[0]), int(color1[1]), int(color1[2])] 

color = list(np.random.random(size=3) * 256)

@st.cache
def draw_line(image,pointA,pointB):
    
    linedImage = cv2.line(image,pointA,pointB,color, thickness=3, lineType=cv2.LINE_AA)
    
    return linedImage

@st.cache
def draw_circle(image,center,radius):
    
    circledImage = cv2.circle(image,center,radius,color, thickness=3, lineType=cv2.LINE_AA)
    
    return circledImage

@st.cache
def draw_filledCircle(image, center,radius):
    
    filledCircle = cv2.circle(image,center,radius,color, thickness=-1, lineType=cv2.LINE_AA)
    
    return filledCircle

@st.cache
def draw_rectangle(image, pointA , pointB):
    
    recentagledImage= cv2.rectangle(image, pointA, pointB,color, thickness=3, lineType=cv2.LINE_AA)
    
    return recentagledImage

@st.cache
def draw_ellipse(image,axis1,axis2,angle,startangle,endangle):
    
    ellipsedImage = cv2.ellipse(image,axis1,axis2,angle,startangle,endangle,color,
                                thickness=3, lineType=cv2.LINE_AA)
    
    return ellipsedImage

@st.cache
def write_text(image,text,org):
    
    text_image = cv2.putText(image,text,org,fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 2,
            color = (250,225,100),thickness =  3, lineType=cv2.LINE_AA)
    
    return text_image





st.title('Image Annotations with OpenCV')

img_file_buffer = st.file_uploader("Upload an image", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))

st.image(image, caption=f"Original Image",use_column_width= True)

height = np.size(image,0)
width = np.size(image,1)



#checkbox for drawing shapes on image

useLine = st.checkbox('Draw a Line')

useCircle = st.checkbox('Draw a Circle')

useRectangle = st.checkbox('Draw a Rectangle')

useEllipse = st.checkbox('Draw a Ellipse')

useText = st.checkbox('Write Text on the image')





if useLine:
    lineImage = image.copy()
    
    
    st.subheader('Draw a Line on the Image')
    
    x1 = st.slider('Select a starting point on X axis',value = 100,max_value =width)
    x2 = st.slider('Select a ending point on X axis',value =200,max_value = width-x1)
    y1 = st.slider('Select a starting point on Y axis',value = 80,max_value =height)
    y2 = st.slider('Select a ending point on Y axis',value =80,max_value =height-y1)
    
    pointA = (x1,y1)
    pointB = (x2,y2)
    
    linedImage = draw_line(lineImage,pointA,pointB)
    
    st.image(
    linedImage, caption=f"Lined_Image", use_column_width=True)
    
    
if useCircle:
    circleImage = image.copy()
    fillCircle  = image.copy()
    X = np.size(image,0)
    Y = np.size(image,1)
    
    st.subheader('Draw a circle')
    
    x1 = st.slider('Select a starting point on X axis',value =100,max_value =X+1)
    y1 = st.slider('Select a starting point on Y axis',value =80,max_value =Y+1)
    
    radius = st.slider('Select the radius from a range of 10 to 1000',min_value = 10, max_value = 1000,value = 100)
    
    center= (x1,y1)
    
    circledImage = draw_circle(circleImage, center,radius)
    filledCircle= draw_filledCircle(fillCircle,center,radius)
    
    st.image(
    circledImage, caption=f"Circle on the Image", use_column_width=True)
    
    st.subheader('Filled Cirlce')
    
    st.image(
       filledCircle, caption=f"Filled Cirlce on the Image", use_column_width=True)
    
if useRectangle:
    imagerect = image.copy()
    
    st.subheader('Draw a Rectangle')
    
    x1 = st.slider('Select a starting point on X axis',value= 300,max_value = width+1)
    x2 = st.slider('Select a ending point on X axis', value = 475,max_value = width-x1+1)
    y1 = st.slider('Select a starting point on Y axis',value = 115,max_value = height+1)
    y2 = st.slider('Select a ending point on Y axis',value = 225,max_value = height-y1+1)
    
    pointA = (x1,y1)
    pointB = (x2,y2)
    
    recentagledImage = draw_rectangle(imagerect,pointA,pointB)
    
    st.image(
       recentagledImage, caption=f"Rectangle on the Image", use_column_width=True)
    

if useEllipse:
    ellipsedImage = image.copy()
    
    
    st.subheader('Draw a Ellipse')
    
    x1 = st.slider('Select a starting point on X axis',value= 415,max_value = width-1)
    x2 = st.slider('Select a ending point on X axis', value = 100,max_value = width-x1-1)
    y1 = st.slider('Select a starting point on Y axis',value = 190,max_value = height-1)
    y2 = st.slider('Select a ending point on Y axis',value = 50,max_value = height-y1-1)
    
    angle =st.slider('Set the angle of Ellipse',max_value =360)
    startangle = st.slider('Set the start angle of the ellipse',max_value =360)
    endangle = st.slider('Set the end angle of the ellipse',value =360,max_value= 360)
    
    axis1 = (x1,y1)
    axis2 = (x2,y2)
    
    imageEllipse = draw_ellipse(ellipsedImage,axis1,axis2,angle,startangle,endangle)
    
    st.image(
       imageEllipse, caption=f"Ellipse on the Image", use_column_width=True)
    

    
if useText:
    
    imageText = image.copy()
    
    st.subheader('Write the Text on the Image')
    
    st.text('Give the Text in put here')
    
    text = st.text_input('',value = 'I am Happy Dog!')
    
    x1 = st.slider('Select a starting point on X axis',value= 50,max_value = width-1)
    y1 = st.slider('Select a starting point on Y axis',value = 350,max_value = height-1)
    
    org = (x1,y1)
    
    textedImage = write_text(imageText,text,org)
    
    st.image(
       textedImage, caption=f"Text on the Image", use_column_width=True)
    
    
st.markdown('''
            # Author \n 
             Hey this is ** Pavan Kunchala ** I hope you like the application \n
            I am looking for ** Collabration ** or ** Freelancing ** in the field of ** Deep Learning ** and 
            ** Computer Vision ** \n
            If you're interested in collabrating you can mail me at ** pavankunchalapk@gmail.com ** \n
            You can check out my ** Linkedin ** Profile from [here](https://www.linkedin.com/in/pavan-kumar-reddy-kunchala/) \n
            You can check out my ** Github ** Profile from [here](https://github.com/Pavankunchala) \n
            You can also check my technicals blogs in ** Medium ** from [here](https://pavankunchalapk.medium.com/)
             
            ''')
    
    
    
    
    
    
    
    

    
    
    
    
    


    
    

    
