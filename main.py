import threading
import wave

import pyaudio


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
OUTPUT_FILE = "audio.wav"


stop_event = threading.Event()


def wait_for_stop():
    input("Press Enter to stop recording...\n")
    stop_event.set()


def main():
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    frames = []
    threading.Thread(target=wait_for_stop, daemon=True).start()

    print("Recording...")

    try:
        while not stop_event.is_set():
            frames.append(stream.read(CHUNK))
    finally:
        stream.stop_stream()
        stream.close()

        sample_width = audio.get_sample_size(FORMAT)
        audio.terminate()

    with wave.open(OUTPUT_FILE, "wb") as file:
        file.setnchannels(CHANNELS)
        file.setsampwidth(sample_width)
        file.setframerate(RATE)
        file.writeframes(b"".join(frames))

    print(f"Saved recording to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
