from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# generate speech by cloning a voice using default settings
def makeWave(text, file_path, speaker_wav):
    tts.tts_to_file(text=text,
                file_path=file_path,
                speaker_wav=speaker_wav,
                language="en")

