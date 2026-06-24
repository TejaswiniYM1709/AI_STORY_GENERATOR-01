import streamlit as st
from story_generator import generate_story

st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="centered"
)

st.title("📖 AI Story Generator")
st.write("Generate amazing stories using AI")

topic = st.text_input("Story Topic")

character = st.text_input("Main Character Name")

genre = st.selectbox(
    "Genre",
    [
        "Romance",
        "Fantasy",
        "Adventure",
        "Comedy",
        "Horror",
        "Sci-Fi",
        "Mystery"
    ]
)

mood = st.selectbox(
    "Mood",
    [
        "Happy",
        "Sad",
        "Emotional",
        "Inspirational",
        "Thrilling"
    ]
)

length = st.selectbox(
    "Story Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

if st.button("Generate Story"):

    if topic and character:

        with st.spinner("Generating story..."):

            story = generate_story(
                topic,
                genre,
                mood,
                length,
                character
            )

        st.success("Story Generated Successfully!")

        st.subheader("Generated Story")

        st.write(story)

        st.download_button(
            label="Download Story",
            data=story,
            file_name="story.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please fill all fields.")