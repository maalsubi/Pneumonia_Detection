import streamlit as st

def display():
    st.write("<h1>PNEUMONIA DETECTOR</h1>",unsafe_allow_html=True)
    st.write("<p style='text-align:justify; font-size: 18px;font-style:italic'>\nEarly detection of pneumonia facilitated by using Deep Learning models with best results is deployed.</p>",unsafe_allow_html=True)
    st.write("<p style='text-align:justify; font-size: 18px;margin: 10px 0;'>\nThis project aims in identification of pneumonia in the patients with the help of X-Ray images. The model which is built provides promising results"+
             "with the accuracy of about 95%. The model is trained with a clinically proved dataset having about 5856 images and several Models were tested and the best two models such as VGG16 and Inception V3 is combined to create an ensembled model.</p>",unsafe_allow_html=True)
    st.write("<h3>Models Description</h3>",unsafe_allow_html=True)
    st.write("<h5>VGG16</h5>",unsafe_allow_html=True)
    st.write("<p style='text-align:justify; font-size: 18px;margin: 10px 0;'>\nThe VGG16 model is known for its deep architecture, which consists of 16 convolutional and fully connected layers. It excels at feature extraction and pattern recognition in images. Its fine-tuned parameters make it highly competent in capturing intricate details in medical images, particularly those with chest X-rays.<br><strong>TEST ACCURACY  90.2243</strong></p>",unsafe_allow_html=True)
    st.write("<h5>InceptionV3</h5>",unsafe_allow_html=True)
    st.write("<p style='text-align:justify; font-size: 18px;margin: 10px 0;'>InceptionV3 is renowned for its efficient use of computational resources while maintaining impressive accuracy. Its inception modules allow it to process images at multiple scales and extract rich features, making it well-suited for complex image classification tasks. When applied to chest X-ray images, InceptionV3 helps identify subtle nuances that may indicate the presence of medical conditions.<br><b>TEST ACCURACY 83.49</b></p>",unsafe_allow_html=True)
    st.write("<h5>Ensembled Model</h5>",unsafe_allow_html=True)
    st.write("<p style='text-align:justify; font-size: 18px;margin: 10px 0;'>By combining VGG16 and InceptionV3, this ensemble model leverages the unique strengths of each architecture. VGG16 excels at capturing detailed features, while InceptionV3 efficiently processes images at different scales. The ensemble technique merges their predictions, resulting in a more comprehensive analysis. This combination not only enhances the model's diagnostic accuracy but also provides a degree of robustness and generalization that is crucial in medical image analysis.<br><b>ACCURACY 96%</b></p>",unsafe_allow_html=True)
    st.write("<h3>Results</h3>",unsafe_allow_html=True)
    st.image("result1.png",caption="Plot of Loss",use_column_width=True)
    st.image("result2.png",caption="Plot of Accuracy",use_column_width=True)