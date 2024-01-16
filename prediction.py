import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import cv2
def show():
    st.write("<h1 style='font-size: 25px;font-style:sans-serif;'>UPLOAD CHEST X-RAY </h2>",unsafe_allow_html=True)

    uploaded_image = st.file_uploader("Choose an image to predict...", type=["jpg", "jpeg", "png"],label_visibility="visible")
    if uploaded_image is not None:
        st.write("Uploaded")
        image = Image.open(uploaded_image)
        #st.image(image, caption="Uploaded Image", use_column_width=True)
        img=np.array(image)
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        target_size = (224, 224)  # Replace with the model's input size
        image_resized = cv2.resize(image_rgb, target_size)
        image_normalized = image_resized / 255.0  # Assuming values are in the range [0, 255]
        image_input = image_normalized.reshape(1,224,224,3)
        if(st.button("CLICK TO PREDICT")):
            predict_image(image_input)

def predict_image(img):
    m1=tf.keras.models.load_model("ensembled.h5")
    pred=m1.predict([img,img])
    data=pred[0]
    labels=['NORMAL','PNEUMONIA']
    chart_container=st.container()
    fig, ax = plt.subplots(figsize=(4,2))
    bar_width = 0.5 
    ax.barh(labels, data, bar_width, align='center')
    ax.set_xlabel('Probability')
    ax.set_title('Bar Chart')
    with chart_container:
        st.pyplot(fig, clear_figure=True, use_container_width=False)
    #st.pyplot(fig)
    #dict_data=dict(zip(labels,data))
    #st.bar_chart(dict_data,use_container_width=True)

