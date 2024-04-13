from TTS.api import TTS
import pydub
from pydub.playback import play
import multiprocessing

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True,)

# generate speech by cloning a voice using default settings
def makeWave(text, file_path, speaker_wav):
    tts.tts_to_file(text=text,
                file_path=file_path,
                speaker_wav=speaker_wav,
                language="en")

def playWave(file_path):
    sound = pydub.AudioSegment.from_wav(file_path)
    sound.export(file_path, format="wav")


def playWaveAsync(file_path):
    sound = pydub.AudioSegment.from_wav(file_path)
    sound.export(file_path, format="wav")
    p = multiprocessing.Process(target=play, args=(sound,))
    p.start()


def makeWaveAndPlay(text, file_path, speaker_wav):
    makeWave(text, file_path, speaker_wav)
    playWaveAsync(file_path)

if __name__ == "__main__":

    makeWaveAndPlay("poopy butt", "test.wav", "data/in.wav")