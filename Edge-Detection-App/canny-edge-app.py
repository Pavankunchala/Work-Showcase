import streamlit as st

from PIL import Image
import numpy as np
import cv2

DEMO_IMAGE = 'edge.jpg'

@st.cache
def edge_detection(image,low_thres,high_thresh):
    
    #convert the image to RGB 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    #convert the image to gray 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    edged = cv2.Canny(image, low_thres,high_thresh)
    
    return edged

    
    



st.title("Canny Edge Detection")

img_file_buffer = st.file_uploader("Upload an image, Make sure you have a clear image", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))
    
st.subheader('Original Image')
st.image(
    image, caption=f"Original Image", use_column_width=True
) 

low_thres = st.slider('Lower threshold for edge detection',min_value = 0 , max_value = 240,value= 80)

high_thresh = st.slider('High threshold for edge detection',min_value = 10, max_value =240,value = 100)

if low_thres > high_thresh:
    
    high_thresh = low_thres +5
    



edges = edge_detection(image,low_thres,high_thresh)

st.subheader('Edged Image')

st.image(
    edges, caption=f"Edged Image", use_column_width=True
) 

st.markdown('''
          # About Author \n 
             Hey this is ** Pavan Kunchala ** I hope you like the application \n
            I am looking for ** Collabration ** or ** Freelancing ** in the field of ** Deep Learning ** and 
            ** Computer Vision ** \n
            I am also looking for ** Job opportunities ** in the field of** Deep Learning ** and ** Computer Vision** 
            if you are intereste in my profile you can check out my resume from 
            [here](https://drive.google.com/file/d/16aKmdHryldvx3OPNwmHhxW-DAoQOypvX/view?usp=sharing)
            \n
            If you're interested in collabrating you can mail me at ** pavankunchalapk@gmail.com ** \n
            You can check out my ** Linkedin ** Profile from [here](https://www.linkedin.com/in/pavan-kumar-reddy-kunchala/) \n
            You can check out my ** Github ** Profile from [here](https://github.com/Pavankunchala) \n
            You can also check my technicals blogs in ** Medium ** from [here](https://pavankunchalapk.medium.com/) \n
            If you are feeling generous you can buy me a cup of ** coffee ** from [here](https://www.buymeacoffee.com/pavankunchala)
             
            ''')




