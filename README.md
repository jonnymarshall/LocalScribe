# LocalScribe

**Overview:**
LocalScribe is a lightweight web application built using Python, HTML, and CSS that uses OpenAI's Whisper to do local, fully private transcription directly within the browser. With LocalTranscribe, users can effortlessly transcribe audio files into text format, generating both a timecoded `.srt` file and a plain text file (`.txt`) with the transcript. This app is designed to provide a seamless transcription experience while prioritizing privacy and security by performing all transcription tasks locally on the user's device.

**Key Features:**
1. **Local Transcription:** Perform transcription tasks directly within the user's browser, ensuring data privacy and security.
  
2. **Multi-Format Output:** Generate both a timecoded `.srt` file and a plain text file (`.txt`) containing the transcript of the audio file.
  
3. **User-Friendly Interface:** Intuitive user interface for uploading audio files and accessing transcribed content effortlessly.

**How It Works:**
1. **Upload Audio File:** Users upload their audio file directly through the web interface.
  
2. **Local Processing:** The app processes the uploaded audio file locally, utilizing a pre-trained model for transcription tasks.
  
3. **Transcription:** The app transcribes the audio file into text format, maintaining accurate timestamps for each segment.
  
4. **Output Generation:** LocalScribe generates both a timecoded `.srt` file and a plain text file (`.txt`) containing the transcribed content.
  
5. **Download Options:** Users can download the generated `.srt` and `.txt` files for further use or reference.

**Usage Scenario:**
Alice, a podcaster, frequently conducts interviews and needs accurate transcripts of her audio recordings. She prefers to maintain privacy and confidentiality by avoiding online transcription services. With LocalTranscribe, Alice can easily upload her audio files and obtain precise transcripts directly within her browser. The generated `.srt` file allows her to synchronize the transcript with the audio, while the `.txt` file serves as a convenient reference document.

**Conclusion:**
LocalTranscribe offers a seamless and privacy-focused solution for users seeking local transcription capabilities. By leveraging modern web technologies and performing all processing tasks locally, LocalTranscribe ensures data privacy while delivering accurate and accessible transcripts for various audio files.

***
# Development Setup

Here are the steps to set up a development environment for LocalScribe.

## Prerequisites

- **Python 3.7 or higher**: Ensure Python and pip (Python package installer) are installed.
- **FFmpeg**: Required for audio processing by Whisper.

## Environment Setup

### 1. Install Homebrew
Install Homebrew, which is used to install FFmpeg and can be used to manage other packages:

- **MacOS**:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  
### 2. Install Python via Homebrew
Once Homebrew is installed, you can use it to install Python:
```
brew install python
```
This will install the latest stable version of Python. After installing, you can verify the installation by checking the version:

```
python3 --version
```

### 3. Install FFmpeg
FFmpeg is required for handling audio files. Install it using the appropriate method for your operating system:
```
brew install ffmpeg
sudo apt install ffmpeg
```

### 4. Install Flask
```
pip install Flask
```

### 5. Install Whisper
```
pip install git+https://github.com/openai/whisper.git
```

### 6. Run the Flask Application
Navigate to the directory containing your app.py and run the application:
```
python app.py
Your Flask server should start, and you can typically access it in your web browser at http://localhost:5000.
```
Once the server is running, navigate to http://localhost:5000 in your web browser to use the application. You can drag and drop audio files to be transcribed.

### Additional Notes
For production environments, additional configuration for security and performance might be necessary. This guide is intended for setting up a development environment only.