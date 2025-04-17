import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(frame):
    """Callback to read samples from buffer."""

    data = stream.read(CHUNK, exception_on_overflow=False)
    samples = np.frombuffer(data, dtype=np.int16)
    line.set_ydata(samples)
    return line,


if __name__ == "__main__":

    # Audio settings
    CHUNK = 1024  # Number of frames per buffer
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # Mono
    RATE = 44100  # Samples per second

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK)
    line, = ax.plot(x, np.random.rand(CHUNK), lw=2)
    ax.set_ylim(-32768, 32767)
    ax.set_xlim(0, CHUNK)

    plt.title("Real-Time Audio Waveform")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")

    # Show live graph.
    ani = animation.FuncAnimation(fig, update, interval=30)
    plt.show()

    # Cleanup the stream.
    stream.stop_stream()
    stream.close()
    p.terminate()
