import pyaudio
import vosk
import json

model_path = "vosk-model-en-us-0.22"  # Update with your model path

model = vosk.Model(model_path)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=4000)

print("Listening...")

rec = vosk.KaldiRecognizer(model, 16000)

while True:
    data = stream.read(4000)
    
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(json.loads(result)["text"])

