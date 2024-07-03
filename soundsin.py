import numpy as np
import sounddevice as sd
import signal
import matplotlib.pyplot as plt

def signal_handler(sig, frame):
    print("\n[!] Stopped\n")
    sd.stop()
    sys.exit(0)

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """
    Generate a sine wave at a given frequency and duration.

    Parameters:
    - frequency: The frequency of the sine wave in Hz.
    - duration: The duration of the sine wave in seconds.
    - sample_rate: The sample rate (default is 44100 Hz).

    Returns:
    - numpy array containing the sine wave.
    """
    print(f"Sample points: {int(sample_rate * duration)}")
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave, t

def play_sine_wave(frequency, duration, sample_rate=44100):
    """
    Play a sine wave at a given frequency and duration.

    Parameters:
    - frequency: The frequency of the sine wave in Hz.
    - duration: The duration of the sine wave in seconds.
    - sample_rate: The sample rate (default is 44100 Hz).
    """
    wave, t = generate_sine_wave(frequency, duration, sample_rate)
    plot_wave(wave, t, frequency, duration, sample_rate)
    sd.play(wave, sample_rate)
    sd.wait()

def plot_wave(wave, t, frequency, duration, sample_rate):
    """
    Plot the generated sine wave.

    Parameters:
    - wave: The numpy array containing the sine wave.
    - t: The numpy array containing the time values.
    - frequency: The frequency of the sine wave in Hz.
    - duration: The duration of the sine wave in seconds.
    - sample_rate: The sample rate.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t, wave)
    plt.title(f'Sine Wave: {frequency} Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.xlim(0, duration if duration < 0.01 else 1/frequency * 5)  # Adjust x-axis for better visualization
    plt.ylim(-1.1, 1.1)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    import sys

    signal.signal(signal.SIGINT, signal_handler)

    if len(sys.argv) < 2:
        print("usage: soundsin.py <frequency>")
        exit(1)

    frequency = float(sys.argv[1])  # Frequency in Hz (A4 note)

    if len(sys.argv) >= 3:
        duration = int(sys.argv[2])
    else:
        duration = 5     # Duration in seconds



    print(f"Playing a {frequency} Hz sine wave for {duration} seconds.")
    play_sine_wave(frequency, duration)

