import streamlit as st
import easyocr

from PIL import Image
import numpy as np
import ssl
import imutils
ssl._create_default_https_context = ssl._create_unverified_context

DEMO_IMAGE = 'demo1.jpeg'
def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text 


st.title("OCR APP")
#st.set_option('deprecation.showfileUploaderEncoding',False)
img_file_buffer = st.file_uploader("Upload an image", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))

st.text('Original Image')

rotated = True

st.image(image)
roated_image = image

col1, col2 = st.beta_columns(2)

with col1:


    rotate_left = st.checkbox('Rotate Left')

    if rotate_left:
        roated_image = imutils.rotate(image, angle=90)
        rotated = True

with col2:
    rotate_right = st.checkbox('Rotate Right ')

    if rotate_right:
        roated_image =imutils.rotate(image, angle=270)
        rotated = True

if rotated:
    st.subheader('Roated Image')
    st.image(roated_image)




#st.image(image)



st.sidebar.subheader("Enter Text")
area = st.sidebar.text_area("Auto Detection Enabled","")

convert = st.button('Convert')

if convert:
    with st.spinner('Extracting Text from given Image'):

        eng_reader = easyocr.Reader(['en'],)
        if rotated:
            print('Roated')

            detected_text = eng_reader.readtext(roated_image)

        else:
             detected_text = eng_reader.readtext(image)
            
        st.subheader('Extracted text is ...')
        text = display_text(detected_text)
        st.write(text)


