# SpeechRateAnalyzer
An intelligent speech analysis tool that transcribes audio, measures speaking duration, and calculates Words Per Minute (WPM) using OpenAI Whisper and FFmpeg.

## 📌 Objective

The objective of this project is to measure a speaker's speaking speed by analyzing an audio recording and calculating:

* Total words spoken
* Speaking duration
* Words Per Minute (WPM)

This project can be used for interview assessment, presentation evaluation, communication analysis, and speech performance measurement.

---

## 🚀 Features

* Speech-to-text transcription using OpenAI Whisper
* Accurate word counting
* Speaking duration calculation
* Words Per Minute (WPM) calculation
* Long pause handling
* Interrupted speech handling
* JSON report generation
* Modular and scalable code structure

---

## 🛠️ Technologies Used

* Python 3
* OpenAI Whisper
* FFmpeg
* JSON

---

## 📂 Project Structure

```text
SpeechRateAnalyzer/
│
├── audio/
│   └── sample.wav.m4a
│
├── src/
│   ├── transcriber.py
│   └── analyzer.py
│
├── speech_report.json
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/SpeechRateAnalyzer.git
cd SpeechRateAnalyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
.\venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Requirements

Install FFmpeg and verify installation:

```bash
ffmpeg -version
```

Required Python packages:

```txt
openai-whisper
torch
librosa
soundfile
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🧠 Working Principle

1. Accept an audio file as input.
2. Convert speech to text using OpenAI Whisper.
3. Count the total spoken words.
4. Calculate actual speaking duration using speech segments.
5. Ignore silent gaps and long pauses.
6. Compute Words Per Minute (WPM).

### Formula

```text
WPM = Total Words / Speaking Duration (minutes)
```

---

## 📊 Sample Output

```json
{
    "total_words": 57,
    "speech_duration_seconds": 31.5,
    "words_per_minute": 109
}
```

---

## ⚠️ Edge Cases Handled

### Long Pauses

Silent gaps between speech segments are ignored while calculating speaking duration.

### Interrupted Speech

Speech broken into multiple segments is analyzed correctly to ensure accurate WPM calculation.

---

## 📄 Output Report

The application automatically generates:

```text
speech_report.json
```

Example:

```json
{
    "total_words": 57,
    "speech_duration_seconds": 31.5,
    "words_per_minute": 109
}
```

---

## 🔮 Future Enhancements

* Real-time speech analysis
* Speaker comparison dashboard
* Web application deployment
* Batch audio processing
* Speech fluency assessment

---

## ✅ Conclusion

Speech Rate Analyzer provides an effective way to evaluate speaking speed from audio recordings. By leveraging OpenAI Whisper and speech segment analysis, the system accurately calculates Words Per Minute (WPM) while handling pauses and interruptions efficiently.
