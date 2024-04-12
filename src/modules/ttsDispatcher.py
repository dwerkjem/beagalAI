from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="Hello world, today is a beautiful",
                file_path="output.wav",
                speaker_wav="in/in.wav",
                language="en")

