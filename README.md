# Voice-Controlled Personal Assistant in Python
This Python script implements a basic voice-controlled personal assistant that can:

Respond to a wake word ("python")

Open popular websites like Google, YouTube, Facebook, and LinkedIn

Play music from a custom library using voice commands

Key Features:
Speech Recognition: Listens for commands using the speech_recognition library and Google’s speech-to-text API.

Text-to-Speech: Gives spoken feedback using pyttsx3.

Web Automation: Opens specific websites in your default browser.

Music Playback: Plays requested songs using a custom musiclibrary (a Python dictionary mapping song names to links).

Wake Word Activation: Only starts listening for commands after detecting the keyword “python”.

How it Works:
Initialization: Speaks "Initializing..." on startup.

Listening Loop: Waits for the user to say "python" as the wake word.

Command Recognition: After hearing "python", listens for the next instruction.

Command Execution: Performs an action (like opening YouTube or playing a song) based on the recognized command.
