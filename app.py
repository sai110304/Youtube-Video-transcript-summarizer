import os
import streamlit as st
import google.generativeai as gai
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
load_dotenv()

gai.configure(api_key=os.getenv('GEMINI_API_KEY'))


pmpt ="Youtube video transcript summarization:  Take the transcript of a youtube video and summarize with each and every point. The transcript will be appended here"

def transcript_extraction(video_url):
    video_id = video_url.split('=')[1]
    transcrip_text = YouTubeTranscriptApi.get_transcript(video_id)
    transcript=""
    for i in transcrip_text:
        transcript+=i['text']+" "
        
    return transcript

def Summarization(text,pmpt):
    model=gai.GenerativeModel("gemini-pro")
    response = model.generate_content(pmpt+text)
    return response.text


st.title("Youtube video transcript summarization")
video_link=st.text_input("Enter the youtube video link")

if video_link:
    video_id=video_link.split('=')[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg")
    
if st.button("Summarize"):
    transcript=transcript_extraction(video_link)
    
    if transcript:
        summary=Summarization(transcript,pmpt)
        st.markdown("### Summary:")
        st.write(summary)