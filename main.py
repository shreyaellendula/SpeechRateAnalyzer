import json

from src.transcriber import transcribe_audio
from src.analyzer import analyze_speech

audio_file = "audio/sample.m4a"

# Transcribe audio
result = transcribe_audio(audio_file)

print("\nTranscript:\n")
print(result["text"])

# Analyze speech
output = analyze_speech(result)

# Display result
print("\nSpeech Analysis Result:\n")
print(output)

# Save JSON report
with open("speech_report.json", "w") as file:
    json.dump(output, file, indent=4)

print("\nReport saved successfully!")