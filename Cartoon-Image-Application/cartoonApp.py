import streamlit as st

from PIL import Image
import numpy as np
import cv2

DEMO_IMAGE = 'BAT.jpg'


#sketching the images
@st.cache
def sketch_img(img):
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #applying median filter
    img_gray = cv2.medianBlur(img_gray,5)
    
    #detecting the images
    edges = cv2.Laplacian(img_gray,cv2.CV_8U,ksize =5)
    
    #threhold for images
    ret, thresholded = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    
    return thresholded

#cartoonize the images
@st.cache
def cartoonize_image(img, gray_mode = False):
    
    thresholded = sketch_img(img)
    
    #applying bilateral fliter wid big numbers to get cartoonnized
    filtered= cv2.bilateralFilter(img,10,250,250)
    
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=thresholded)
    
    if gray_mode:
        return cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)
    
    return cartoonized

st.title('Cartooning the Images with OpenCV')

img_file_buffer = st.file_uploader("Upload an image", type=[ "jpg", "jpeg",'png'])


if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))

st.image(image, caption=f"Original Image",use_column_width= True)

st.subheader('Sketch Image')

custom_sketch_image = sketch_img(image)
custom_cartonized_image = cartoonize_image(image)
custom_cartonized_image_gray = cartoonize_image(image, True)


sketch_gray, sketch_color = cv2.pencilSketch(image, sigma_s=30, sigma_r=0.1, shade_factor=0.1)
stylizated_image = cv2.stylization(image, sigma_s=60, sigma_r=0.07)

st.image(custom_sketch_image,caption=f"Sketch Image",use_column_width= True)

st.subheader('Cartoonized Image')
st.image(custom_cartonized_image,caption=f"Cartoonized Image",use_column_width= True)

st.subheader('Cartoonized Image Gray')
st.image(custom_cartonized_image_gray,caption=f"Cartoonized Image Gray",use_column_width= True)

st.subheader('PencilSketch Color')
st.image(sketch_color,caption=f"Pencil Sketch Color",use_column_width= True)


st.subheader('PencilSketch Gray')
st.image(sketch_gray,caption=f"Pencil Sketch Gray",use_column_width= True)



st.subheader('Stylized Image')
st.image(stylizated_image,caption=f"Pencil Sketch Color",use_column_width= True)


st.markdown('''
          # Author \n 
             Hey this is ** Pavan Kunchala ** I hope you like the application \n
            I am looking for ** Collabration ** or ** Freelancing ** in the field of ** Deep Learning ** and 
            ** Computer Vision ** \n
            If you're interested in collabrating you can mail me at ** pavankunchalapk@gmail.com ** \n
            You can check out my ** Linkedin ** Profile from [here](https://www.linkedin.com/in/pavan-kumar-reddy-kunchala/) \n
            You can check out my ** Github ** Profile from [here](https://github.com/Pavankunchala) \n
            You can also check my technicals blogs in ** Medium ** from [here](https://pavankunchalapk.medium.com/) \n
            If you are feeling generous you can buy me a cup of ** coffee ** from [here](https://www.buymeacoffee.com/pavankunchala)
             
            ''')


