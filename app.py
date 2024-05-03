from flask import Flask, request, jsonify, render_template
import os
import whisper
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)  # Save the original audio file

    # Process the file for transcription
    transcription, srt_content = transcribe_audio(filepath)

    # Save the transcription to a .txt file
    txt_path = os.path.splitext(filepath)[0] + '_transcript.txt'
    with open(txt_path, 'w') as txt_file:
        txt_file.write(transcription)
        print(f"Transcription saved to {txt_path}")

    # Save the srt content to a .srt file
    srt_path = os.path.splitext(filepath)[0] + '.srt'
    with open(srt_path, 'w') as srt_file:
        srt_file.write(srt_content)
        print(f"SRT saved to {srt_path}")

    return jsonify({'message': 'File uploaded and processed', 'txt_file': txt_path, 'srt_file': srt_path})


def transcribe_audio(filepath):
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    print("Model loaded. Transcribing...")
    result = model.transcribe(filepath)
    print("Transcription completed.")

    # Assuming result contains a 'segments' list of dicts with 'start', 'end', and 'text'
    if 'segments' in result:
        transcription = format_timecoded_transcript(result['segments'])
    else:
        transcription = result['text']

    srt_content = result.get('srt', 'SRT format not available')  # Check if SRT is directly available
    return transcription, srt_content

def format_timecoded_transcript(segments):
    timecoded_transcript = ""
    for segment in segments:
        start_time = format_time(segment['start'])
        end_time = format_time(segment['end'])
        text = segment['text']
        timecoded_transcript += f"{start_time} --> {end_time}\n{text}\n\n"
    return timecoded_transcript

def format_time(seconds):
    # Convert seconds to hour:minute:second,millisecond format
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:06.3f}".replace('.', ',')

def format_srt(transcription_segments):
    srt_content = ""
    for index, segment in enumerate(transcription_segments, start=1):
        start_time = format_time(segment['start'])
        end_time = format_time(segment['end'])
        text = segment['text']
        srt_content += f"{index}\n{start_time} --> {end_time}\n{text}\n\n"
    return srt_content


if __name__ == '__main__':
    app.run(debug=True)
