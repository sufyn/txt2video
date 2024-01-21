import nltk
nltk.download('punkt')
nltk.download('stopwords')
import streamlit as st
import os
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from googletrans import Translator
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

model_name = "facebook/bart-large-cnn"  # Remove the transformer model
# Remove the following two lines
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def text_to_audio(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    return tts

def generate_summary(text):
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate word frequencies
    word_frequencies = FreqDist(filtered_words)

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word.isalnum() and word in word_frequencies:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]

    # Get the summary with top 2 sentences
    num_sentences = int(len(sentences) * 0.5)
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    return summary

def main():
    st.title("Text to Video with Streamlit")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        pdf_path = os.path.join("uploads", "input.pdf")
        with open(pdf_path, "wb") as file:
            file.write(uploaded_file.getvalue())

        extracted_text = extract_text_from_pdf(pdf_path)

        # User selects the language
        selected_language = st.selectbox("Select Language:", ["en", "es", "fr", "de"])

        # Generate summary using NLTK instead of transformers
        summary = generate_summary(extracted_text)

        # Translate summary to the selected language
        translated_text = translate_text(summary, target_language=selected_language)

        # Convert translated text to audio
        audio_result = text_to_audio(translated_text, language=selected_language)
        audio_path = os.path.join("static", "audio.mp3")
        audio_result.save(audio_path)

        # Load the video clip of a person speaking
        person_speaking_clip = VideoFileClip(os.path.join("static", "background.mp4"))

        # Load the audio file
        audio_clip = AudioFileClip(audio_path)

        # Calculate the number of times the video needs to be looped
        num_loops = int(audio_clip.duration / person_speaking_clip.duration)

        # Create a list of video clips by looping the person speaking clip
        video_clips = [person_speaking_clip] * num_loops

        # Concatenate the video clips to create the final video
        final_video_clip = concatenate_videoclips(video_clips, method="compose")

        # Set the audio of the final video clip to the desired audio
        final_video_clip = final_video_clip.set_audio(audio_clip)

        # Export the final video
        video_path = os.path.join("static", "output_video.mp4")
        final_video_clip.write_videofile(video_path, codec="libx264", audio_codec="aac")

        st.video(video_path)

if _name_ == "_main_":
    main()
