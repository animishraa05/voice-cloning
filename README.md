# Voice Cloning with Coqui XTTS-v2

A simple python script for zero-shot voice cloning using Coqui TTS (XTTS-v2). You can clone a voice using a short 6-10 second reference audio clip.

## Prerequisites

- Python 3.9 - 3.11 recommended
- An NVIDIA GPU is highly recommended for faster inference, but CPU works as well.

## Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script by providing the text you want to synthesize and a reference audio file (`.wav` format, 6-10 seconds long, clean voice without background noise).

```bash
python main.py --text "Hello, this is a test of voice cloning." --speaker_wav reference.wav --output output.wav
```

### Arguments

- `--text`: The text you want the cloned voice to say.
- `--speaker_wav`: Path to the reference audio file (`.wav`).
- `--language`: The language of the output text (default is `en`).
- `--output`: Path to save the generated audio (default is `output_cloned.wav`).

## Note

- The first time you run the script, it will download the XTTS-v2 model automatically (around 1.5 - 2 GB).
- By using this script, you automatically accept the Coqui Public Model License.
