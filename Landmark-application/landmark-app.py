from PIL import Image
import numpy as np
import cv2
import tensorflow as tf
import dlib
import streamlit as st

# Define what landmarks you want:
JAWLINE_POINTS = list(range(0, 17))
RIGHT_EYEBROW_POINTS = list(range(17, 22))
LEFT_EYEBROW_POINTS = list(range(22, 27))
NOSE_BRIDGE_POINTS = list(range(27, 31))
LOWER_NOSE_POINTS = list(range(31, 36))
RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))
MOUTH_OUTLINE_POINTS = list(range(48, 61))
MOUTH_INNER_POINTS = list(range(61, 68))
ALL_POINTS = list(range(0, 68))

@st.cache
def draw_shape_lines_all(np_shape, image):
    """Draws the shape using lines to connect between different parts of the face(e.g. nose, eyes, ...)"""

    draw_shape_lines_range(np_shape, image, JAWLINE_POINTS)
    draw_shape_lines_range(np_shape, image, RIGHT_EYEBROW_POINTS)
    draw_shape_lines_range(np_shape, image, LEFT_EYEBROW_POINTS)
    draw_shape_lines_range(np_shape, image, NOSE_BRIDGE_POINTS)
    draw_shape_lines_range(np_shape, image, LOWER_NOSE_POINTS)
    draw_shape_lines_range(np_shape, image, RIGHT_EYE_POINTS, True)
    draw_shape_lines_range(np_shape, image, LEFT_EYE_POINTS, True)
    draw_shape_lines_range(np_shape, image, MOUTH_OUTLINE_POINTS, True)
    draw_shape_lines_range(np_shape, image, MOUTH_INNER_POINTS, True)

@st.cache
def draw_shape_lines_range(np_shape, image, range_points, is_closed=False):
    """Draws the shape using lines to connect the different points"""

    np_shape_display = np_shape[range_points]
    points = np.array(np_shape_display, dtype=np.int32)
    cv2.polylines(image, [points], is_closed, (255, 255, 0), thickness=2, lineType=cv2.LINE_8)
    
@st.cache
def draw_shape_points_pos_range(np_shape, image, points):
    """Draws the shape using points and position for every landmark filtering by points parameter"""

    np_shape_display = np_shape[points]
    draw_shape_points_pos(np_shape_display, image)

@st.cache
def draw_shape_points_pos(np_shape, image):
    """Draws the shape using points and position for every landmark"""

    for idx, (x, y) in enumerate(np_shape):
        # Draw the positions for every detected landmark:
        cv2.putText(image, str(idx + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255))

        # Draw a point on every landmark position:
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)


@st.cache
def draw_shape_points_range(np_shape, image, points):
    """Draws the shape using points for every landmark filtering by points parameter"""

    np_shape_display = np_shape[points]
    draw_shape_points(np_shape_display, image)

@st.cache
def draw_shape_points(np_shape, image):
    """Draws the shape using points for every landmark"""

    # Draw a point on every landmark position:
    for (x, y) in np_shape:
        cv2.circle(image, (x, y), 3, (255, 0, 0), -3)

@st.cache
def shape_to_np(dlib_shape, dtype="int"):
    """Converts dlib shape object to numpy array"""

    # Initialize the list of (x,y) coordinates
    coordinates = np.zeros((dlib_shape.num_parts, 2), dtype=dtype)

    # Loop over all facial landmarks and convert them to a tuple with (x,y) coordinates:
    for i in range(0, dlib_shape.num_parts):
        coordinates[i] = (dlib_shape.part(i).x, dlib_shape.part(i).y)

    # Return the list of (x,y) coordinates:
    return coordinates

#the Demo image we will be using 
DEMO_IMAGE = 'landmark.jpg'

p = "shape_predictor_68_face_landmarks.dat"

# Initialize frontal face detector and shape predictor:
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

@st.cache
def landmark_detection(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    rects = detector(gray,0)
    
    for (i, rect) in enumerate(rects):
        # Draw a box around the face:
        cv2.rectangle(image, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 0), 2)

        # Get the shape using the predictor:
        shape = predictor(gray, rect)

        # Convert the shape to numpy array:
        shape = shape_to_np(shape)

        #Draw all lines connecting the different face parts:
        draw_shape_lines_all(shape, image)

        # Draw jaw line:
        #draw_shape_lines_range(shape, image, JAWLINE_POINTS)

        # Draw all points and their position:
        #draw_shape_points_pos(shape, image)
        # You can also use:
        #draw_shape_points_pos_range(shape, image, ALL_POINTS)

        # Draw all shape points:
        draw_shape_points(shape, image)

        # Draw left eye, right eye and bridge shape points and positions
        #draw_shape_points_pos_range(shape, image, LEFT_EYE_POINTS + RIGHT_EYE_POINTS + NOSE_BRIDGE_POINTS)
        
    return image


#title of the image
st.title('Face Landmark Detection')

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

landmarked_image =landmark_detection(image)

st.subheader('Landmarked Image')
st.image(
    landmarked_image, caption=f"Landmarked Image", use_column_width=True
) 

    
st.markdown('''
          # About Author \n 
             Hey this is ** Pavan Kunchala ** I hope you like the application \n
             
            I am looking for ** Collabration **,** Freelancing ** and  ** Job opportunities ** in the field of ** Deep Learning ** and 
            ** Computer Vision **  if you are interested in my profile you can check out my resume from 
            [here](https://drive.google.com/file/d/1Mj5IWmkkKajl8oSAPYtAL_GXUTAOwbXz/view?usp=sharing)\n
            
            If you're interested in collabrating you can mail me at ** pavankunchalapk@gmail.com ** \n
            You can check out my ** Linkedin ** Profile from [here](https://www.linkedin.com/in/pavan-kumar-reddy-kunchala/) \n
            You can check out my ** Github ** Profile from [here](https://github.com/Pavankunchala) \n
            You can also check my technicals blogs in ** Medium ** from [here](https://pavankunchalapk.medium.com/) \n
            If you are feeling generous you can buy me a cup of ** coffee ** from [here](https://www.buymeacoffee.com/pavankunchala)
             
            ''')


