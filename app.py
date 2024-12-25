import streamlit as st
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from datetime import datetime
from io import BytesIO
buf = BytesIO()


ARCHITECT = "Tea[M]edia@COTLUnilorin"
BIO_URL   = "mailto:team.mediacotl@gmail.com"
APPNAME   = "MakeDP"

st.set_page_config(icon="favicon.png", title=f"Wish | {APPNAME}")
# your loved ones --> info


# st.image("will-be-at-carol-banner.png", use_column_width=True)
st.title("✨ Wish")
st.caption("Wish your loved ones Merry Christmas")


def image_side_text(ist_holder, image_url="favicon.png", image_width=44, markdown=f"<h1 style=\"margin-top: -0.5rem;\">{APPNAME}</h1>", columns=[4, 20]):
    ist_var = ist_holder.container()
    col1, col2 = ist_holder.columns(columns)
    with ist_var:
        with col1:
            st.image(image_url, width=image_width)
        with col2:
            st.markdown(markdown, unsafe_allow_html=True)


with st.container(border=True):
    base_image = st.file_uploader("Upload Your Photo", type=["jpg", "jpeg", "png"])
    design_image = "design.png"
    st.button("Generate")

# if base_image:
with st.container(border=True):

    def aspect_ratio(ar_width, original_width, original_height):
        ar_value = original_height / original_width
        ar_height = int(ar_width * ar_value)
        return (ar_width, ar_height)

    if base_image and design_image:
        # Open the images
        base_img = Image.open(base_image)
        design_img = Image.open(design_image)
        duplicated_base_image = base_img.resize(aspect_ratio(1000, base_img.width, base_img.height))

        crop_box = (0, 0, 2000, 2000)
        base_img = base_img.resize((2000, 2000))
        base_img = base_img.filter(ImageFilter.GaussianBlur(5))

        design_width = design_img.width
        design_height = design_img.height
        design_img = design_img.resize((design_width, design_height))

        # Choose placement coordinates
        x_offset = st.slider("Horizontal Image Position", 0, 2000, 208)
        y_offset = st.slider("Vertical Image Position", -400, 2000, 525)

        # Create a copy of the base image to overlay on
        combined_image = base_img.copy()
        combined_image.paste(duplicated_base_image, (x_offset, y_offset))
        combined_image.paste(design_img, (0, 0), design_img)

        # Display the resulting image
        st.image(combined_image, caption="Combined Image", use_column_width=True)

        # Option to save the combined image
        dp_filename = f"wmc24makedp-{datetime.now().timestamp()}.jpg"
        # combined_image.save(dp_filename)
        buffered = BytesIO()
        combined_image.save(buffered, format="JPEG")
        save_button = st.download_button("Download Image", data=buffered.getvalue(), file_name=dp_filename, mime="image/jpeg")
        if save_button:
            st.success(f"Image saved as {dp_filename}")

st.markdown("#")

image_side_text(st, columns=[2.5, 37], markdown=f"<h1 style=\"margin-top: -1.3rem;\">{APPNAME}</h1>")
st.markdown("####")
image_side_text(st, image_url="tcitrogg-logo-purple.svg", image_width=25, markdown=f"Made by <br>[yours **{ARCHITECT}**](mailto:team.mediacotl@gmail.com)", columns=[2.5, 65])