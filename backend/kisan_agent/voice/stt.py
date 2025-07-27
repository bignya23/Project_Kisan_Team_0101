import os
from google.cloud import texttospeech, speech
import time
import uuid
from dotenv import load_dotenv

load_dotenv()

# ---------- TEXT TO SPEECH FUNCTIONS ----------

def text_to_speech_female_hindi(text):
    """Converts text to female Hindi voice and saves as MP3"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALs")
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    uuid_ = uuid.uuid4()
    os.makedirs("../../../frontend/public/assets", exist_ok=True)
    output_file = f"../../../frontend/public/assets/female_{uuid_}.mp3"

    voice = texttospeech.VoiceSelectionParams(
        language_code="hi-IN",
        name="hi-IN-Chirp3-HD-Aoede",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    print(f"Audio content written to {output_file}")
    return f"/public/assets/female_{uuid_}.mp3"


def text_to_speech_male_hindi(text):
    """Converts text to male Hindi voice and saves as MP3"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALs")
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    uuid_ = uuid.uuid4()
    os.makedirs("../../../frontend/public/assets", exist_ok=True)
    output_file = f"../../../frontend/public/assets/male_output.mp3"

    voice = texttospeech.VoiceSelectionParams(
        language_code="hi-IN",
        name="hi-IN-Chirp3-HD-Charon",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    print(f"Audio content written to {output_file}")
    return f"/public/assets/male_output.mp3"


# ---------- SPEECH TO TEXT FUNCTION ----------

def speech_to_text_hindi(audio_file_path):
    """Converts Hindi speech (FLAC/WAV/LINEAR16) to text"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALs")
    client = speech.SpeechClient()

    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, 
        sample_rate_hertz=16000,  
        language_code="hi-IN"
    )

    response = client.recognize(config=config, audio=audio)

    text_result = " ".join([result.alternatives[0].transcript for result in response.results])
    print(f"Recognized Text: {text_result}")
    return text_result


# ---------- MAIN TESTING ----------

if __name__ == "__main__":
    start = time.time()

    # TTS test
    print(text_to_speech_female_hindi("आँगन मेरा, गलियां ये मेरी, सूनी लगे हर दिन दोपहरी"))

    # STT test (replace with your recorded WAV/FLAC file)
    # print(speech_to_text_hindi("test_audio.wav"))

    end = time.time()
    print(f"Time Taken: {end - start} seconds")
