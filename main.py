import torch
import argparse
import os
from TTS.api import TTS

def clone_voice(text, speaker_wav, language="en", output_path="output_cloned.wav"):
    """
    Clones a voice from a reference audio file and generates speech from text.
    """
    if not os.path.exists(speaker_wav):
        print(f"Error: Reference audio file '{speaker_wav}' not found.")
        return

    print("Checking for GPU availability...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    print("Loading XTTS-v2 model (this may take a while on the first run as it downloads the model)...")
    try:
        # Initialize the model
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Note: You may need to agree to the Coqui Public Model License by setting the environment variable COQUI_TOS_AGREED=1")
        return

    print(f"Generating speech for text: '{text}'...")
    print(f"Using reference audio: '{speaker_wav}'")
    
    # Generate the audio
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language=language,
        file_path=output_path
    )

    print(f"Audio generated successfully! Saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Voice Cloning using Coqui XTTS-v2")
    parser.add_argument("--text", type=str, required=True, help="Text to convert to speech")
    parser.add_argument("--speaker_wav", type=str, required=True, help="Path to a clean 6-10s WAV file of the target voice")
    parser.add_argument("--language", type=str, default="en", help="Language code (e.g., 'en', 'es', 'fr')")
    parser.add_argument("--output", type=str, default="output_cloned.wav", help="Output WAV file path")

    args = parser.parse_args()

    # Automatically agree to the Coqui TOS to avoid interactive prompts in scripts
    os.environ["COQUI_TOS_AGREED"] = "1"

    clone_voice(args.text, args.speaker_wav, args.language, args.output)
