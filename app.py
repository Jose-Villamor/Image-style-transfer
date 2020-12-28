from PIL import Image
import streamlit as st

import style_transfer
styles = ["Candy","Composition 6","Feathers","La muse","Mosaic","Starry night", "The scream", "The wave", "Udnie"]

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

st.subheader("Jose Villamor")

html_temp = """
    <div style="background:#581f75;padding:10px">
    <h2 style="color:white;text-align:center;"> Image style transfer </h2>
    </div>
            """
st.markdown(html_temp, unsafe_allow_html = True)

#image = Image.open('sectors.png')
#st.image(image, use_column_width=True)

st.write("Style transfer allows you to modify an image so it resembles a particular style.") 
st.write("Upload an image, select an style and them click the buttom.") 

st.write("**Upload an image**")
image = st.file_uploader(" ")

st.write("**Choose an style**")
style = st.selectbox("", styles)


st.write("**Click the buttom**")
if st.button("Style Transfer"):
    if image is not None and style is not None:
        res = style_transfer.transfer(style, image)
        st.image(res, width=700)
        
if st.button("Download image"):
    img = Image.open("image.jpg")
    img.save(f"image_{style}.jpg")
        
st.write("**If you want to know more about this project or others that I have done visit my github account: https://github.com/Jose-Villamor/Kaggle-Notebooks**")        

st.subheader("Model description")
st.write("To make this website app I use pretrained models obtained from the github account of Justin Johnson (https://github.com/jcjohnson/neural-style). The app architecture is really simple and consist of 2 functions: one to load the pretrained style model and another one to apply it to the uploaded image. Additionally, I use  an eassy but useful library called streamlit for the frontend.")