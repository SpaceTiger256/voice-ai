# Import necessary libraries
import threading          # For running tasks in parallel (recording, spinner, input)
import sys                # For writing to terminal (spinner animation)
import time               # For delays (spinner timing)
import wave               # For saving audio as a .wav file

import pyaudio            # For recording audio from microphone
import numpy as np        # (Not used here, but commonly used for audio processing)
import matplotlib.pyplot as plt  # (Not used here either, can be removed)

import speech_recognition as sr  # For speech-to-text
from speech_recognition import AudioData  # For wrapping raw audio data


# Create a global event to signal when to stop recording
stop = threading.Event()


# This function waits for user input (Enter key) to stop recording
def wait_stop():
    input("\nPress Enter to stop recording...\n")
    stop.set()  # Signal all threads to stop


# This function shows a spinning animation while recording
def spinner():
    while not stop.is_set():  # Run until stop is triggered
        for c in "|/-\\":     # Simple spinner characters
            sys.stdout.write(f"\rRecording... {c}")  # Overwrite same line
            sys.stdout.flush()
            time.sleep(0.1)
    print("\nDone recording!")


# This function records audio from the microphone
def record():
    # Create PyAudio instance
    p = pyaudio.PyAudio()

    # Open input audio stream
    stream = p.open(
        format=pyaudio.paInt16,  # 16-bit audio
        channels=1,              # Mono audio
        rate=16000,              # Sample rate (good for speech)
        input=True,              # Input device (microphone)
        frames_per_buffer=1024   # Chunk size
    )

    # Start background threads
    threading.Thread(target=wait_stop, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()

    frames = []  # List to store audio chunks

    # Keep recording until stop event is triggered
    while not stop.is_set():
        data = stream.read(1024)  # Read audio chunk
        frames.append(data)

    # Stop and clean up stream
    stream.stop_stream()
    stream.close()

    # Get sample width (bytes per sample)
    width = p.get_sample_size(pyaudio.paInt16)

    p.terminate()

    # Return raw audio data + metadata
    return b"".join(frames), 16000, width


# This function saves the recorded audio to a WAV file
def save(data, rate, width, file="recording.wav"):
    with wave.open(file, 'wb') as f:
        f.setnchannels(1)       # Mono
        f.setsampwidth(width)   # Sample width
        f.setframerate(rate)    # Sample rate
        f.writeframes(data)     # Write raw audio data


# This function converts speech to text using Google API
def transcribe(data, rate, width):
    recognizer = sr.Recognizer()

    try:
        # Wrap raw audio into AudioData object
        audio = AudioData(data, rate, width)

        # Use Google's speech recognition
        text = recognizer.recognize_google(audio)

        print("Transcription:", text)

    except Exception as e:
        print("Transcription Failed:", e)


# -------------------------
# MAIN PROGRAM FLOW
# -------------------------

if __name__ == "__main__":
    print("Starting recording...")

    # Record audio
    data, rate, width = record()

    # Save to file
    save(data, rate, width)

    # Transcribe audio
    transcribe(data, rate, width)