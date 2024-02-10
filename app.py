# Imports
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

# Page Configuration
st.set_page_config(page_title="WordCloud",layout="wide",page_icon=":cloud:")

# Header
st.header("Word Cloud Generator")

# Get the text
text = st.text_area(label="Enter the text/Paste the text")
generate = st.button(label="Generate",use_container_width=True)


if text and generate:
    # Generate word cloud
    wordcloud = WordCloud(width=600, height=300, background_color='white').generate(text)

    # Display the generated word cloud
    fig,ax = plt.subplots()
    ax.imshow(wordcloud,interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    # Download the image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    st.download_button(label="Download Image", data=image_stream, file_name='wordcloud.png', mime='image/png',use_container_width=True)

elif not text and generate:
    st.warning("Please enter the text first")
else:
    st.info("Paste the text and click generate")