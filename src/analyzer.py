def analyze_speech(result):

    transcript = result["text"]

    # Count words
    word_count = len(transcript.split())

    # Calculate speaking duration
    speech_duration = 0

    for segment in result["segments"]:
        speech_duration += (
            segment["end"] - segment["start"]
        )

    # Calculate WPM
    minutes = speech_duration / 60

    if minutes > 0:
        wpm = round(word_count / minutes)
    else:
        wpm = 0

    return {
        "total_words": word_count,
        "speech_duration_seconds": round(
            speech_duration, 2
        ),
        "words_per_minute": wpm
    }