from openai import OpenAI
import streamlit as st
from PIL import Image
from apikey import apikey
from streamlit_carousel import carousel #Display Multiple images generated like a slide show

st.set_page_config(page_title="DALLE Image Generator", page_icon=":camera", layout="wide")

#FRONTEND
st.title("Mukhi's DALLE-3 Image Generator")
st.subheader("Powered by the Worlds most powerful Image Genertion API DALL-E-3")
img_description = st.text_input("Enter Image Description")
num_of_images = st.number_input("Select number of images you want togenerate",min_value=1,max_value=5,value=1)

#Initialize Image Generation Client
client=OpenAI(api_key=apikey)

#Function
def generate_img(img_description,num_of_images):
 
    images = []

    for i in range(num_of_images):
        img_responce = client.images.generate(
            model = "dall-e-2",
            prompt = img_description,
            size = "1024x1024",
            quality = "standard",
            n = 1
        )
        img_url = img_responce.data[0].img_url
        
        new_img = single_img.copy()
        new_img["title"] = f"Image {i+1}"
        new_img["text"] = img_description
        new_img["img"] = img_url

        images.append(new_img)

    return images

#For Carousel
single_img = dict(
    title="",
    text = "",
    interval = None,
    img=""
)

if st.button("GENERATE"):
    generate_img = generate_img(img_description, num_of_images)
    carousel(items = generate_img,width=1)

