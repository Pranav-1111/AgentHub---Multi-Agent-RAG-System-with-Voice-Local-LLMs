import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile
import pyttsx3
from langchain.llms import LlamaCpp

class VoiceAgent:
    def __init__(self):
        self.model = whisper.load_model("small")
        self.tts = pyttsx3.init()
        self.llm = LlamaCpp(
            model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            temperature=0.3,
            max_tokens=256,
            n_ctx=2048,
            verbose=False,
        )

    def record_audio(self, duration=5, samplerate=16000):
        print("🎤 Speak your query after the beep... (Recording for 5 seconds)")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        return audio, samplerate

    def transcribe_audio(self, audio, samplerate):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            scipy.io.wavfile.write(tmpfile.name, samplerate, audio)
            result = self.model.transcribe(tmpfile.name)
        return result["text"]

    def ask_llm(self, query):
        return self.llm.invoke(query)

    def speak_response(self, text):
        print(f"🧠 LLM Response: {text}")
        self.tts.say(text)
        self.tts.runAndWait()

    def run(self):
        audio, sr = self.record_audio()
        query = self.transcribe_audio(audio, sr)
        print(f"🗣️ You said: {query}")
        response = self.ask_llm(query)
        self.speak_response(response)
        return query, response


# ✅ Add this to run from terminal
if __name__ == "__main__":
    print("🤖 AgentHub Voice Agent")
    agent = VoiceAgent()
    try:
        while True:
            print("\n🔁 Starting new voice interaction... (Press Ctrl+C to stop)")
            query, response = agent.run()
    except KeyboardInterrupt:
        print("\n👋 Voice Agent stopped by user.")
