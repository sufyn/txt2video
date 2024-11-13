# Text to Video with Streamlit

## Overview

This project allows you to convert text from a PDF into a video with an audio narration, all using the power of Python libraries like NLTK, Streamlit, MoviePy, and gTTS (Google Text-to-Speech). The text is first extracted from the PDF, summarized, translated (if necessary), and then converted into audio. The audio is synchronized with a video clip of a person speaking, generating an engaging video with voiceover.

## Features

- **PDF Text Extraction**: Extracts text from uploaded PDF files.
- **Text Summarization**: Uses NLTK to summarize the extracted text.
- **Text Translation**: Supports translation of the summarized text to different languages.
- **Text-to-Speech**: Converts the translated text into an audio file using gTTS.
- **Video Creation**: Combines a video of a person speaking with the generated audio to create a synchronized video.
- **Streamlit Interface**: Easy-to-use web interface for users to upload PDFs and interact with the system.

## Installation

To use this project, ensure that you have Python 3.x installed. Then, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/text-to-video-streamlit.git
   cd text-to-video-streamlit
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   - `nltk`: For text processing and summarization.
   - `streamlit`: For the web app interface.
   - `gTTS`: For text-to-speech conversion.
   - `moviepy`: For video editing.
   - `googletrans`: For translation.
   - `PyPDF2`: For PDF text extraction.

3. Download the necessary NLTK resources:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload a PDF file.

4. Choose a language for translation (English, Spanish, French, or German).

5. The app will:
   - Extract text from the uploaded PDF.
   - Generate a summary of the text.
   - Translate the summary to the selected language.
   - Convert the translated text to speech.
   - Create a video of a person speaking with the generated audio.

6. Watch and download the final video output.

## Code Explanation

### Text Extraction

The function `extract_text_from_pdf` uses `PyPDF2` to extract text from each page of the uploaded PDF.

### Text Summarization

The `generate_summary` function:
- Tokenizes the text into sentences and words.
- Removes stopwords.
- Calculates word frequencies and assigns sentence scores based on word frequency.
- Selects the top 50% of sentences to create a summary.

### Translation

The `translate_text` function uses `googletrans` to translate the summary into the selected language.

### Text-to-Speech

The `text_to_audio` function uses `gTTS` to convert the translated text into audio.

### Video Creation

The `main` function:
- Takes the audio and video clip of a person speaking.
- Loops the video clip to match the audio length.
- Combines the video clips and sets the audio.
- Saves and displays the final video.

## Example

To test the application:

1. Upload a PDF containing text.
2. Select the desired language for translation (e.g., Spanish).
3. Watch the generated video with synchronized audio in your selected language.

## Requirements

- Python 3.x
- External resources:
  - A video clip (`background.mp4`) to serve as the base video for speaking.
  - Audio generation capabilities with `gTTS`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- `gTTS` for text-to-speech functionality.
- `MoviePy` for video editing.
- `PyPDF2` for extracting text from PDFs.
- `NLTK` for text processing and summarization.
- `Streamlit` for building the web interface.
- `googletrans` for translation capabilities.

## Contact

For questions or suggestions, feel free to reach out to me at [sufyaan4guys@gmail.com].
