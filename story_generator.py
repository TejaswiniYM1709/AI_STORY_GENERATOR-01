import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")
def generate_story(topic, genre, mood, length, character):
    prompt = f"""
    Write a {length} {genre} story.
    Topic: {topic}
    Main Character: {character}
    Mood: {mood}
    Requirements:
    - Strong beginning
    - Interesting plot
    - Emotional development
    - Creative ending
    - Use vivid descriptions
    """
    response = model.generate_content(prompt)
    return response.text
