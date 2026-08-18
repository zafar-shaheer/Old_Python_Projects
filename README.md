    # Early Python Projects
This repository collects four personal Python projects I built between 2019 and 2021, while learning and experimenting with the language on my own. They cover a mix of basic automation, computer vision, file processing, and a simple encoding/decoding scheme. None of them were built as production software — they're kept here as a record of early, hands-on experimentation with Python across a few different problem areas.

## Projects

| Project | Year | Description | Technologies |
|---|---|---|---|
| `Encrypter_Decrypter.py` | 2021 | Encodes and decodes text from a Word document using a custom character-to-binary mapping | Python, python-docx |
| `Nmap - Zenmap GUI.py` | 2020 | Automates repetitive scan-and-save steps in the Nmap/Zenmap GUI for a list of IP addresses | Python, PyAutoGUI |
| `Seperating Frame.py` | 2020 | Extracts individual frames from a video file and saves them as resized JPEG images | Python, OpenCV |
| `vid rec and save.py` | 2019 | Records webcam video and saves it as an AVI file | Python, OpenCV |

### Encrypter_Decrypter.py (2021)

A basic encoding/decoding tool built around a manually defined dictionary that maps individual characters to 8-bit binary strings. The script reads the first paragraph of a Word document, converts it to lowercase, and — in encrypt mode — replaces each character with its binary code to produce an encoded string, which is written out to a new `.docx` file. In decrypt mode, it does the reverse: it reads the encoded document 8 characters at a time and looks each chunk up in the same dictionary to reconstruct the original text.

This is a substitution scheme based on a fixed lookup table, not a cryptographic algorithm — there's no key, hashing, or standard encryption method involved. It's a project built to explore how text could be transformed and reversed programmatically, not a security tool.

- Runs from the command line and prompts for encrypt/decrypt mode, file paths, and filenames.
- Only reads the first paragraph of the source document.
- Main concepts: dictionary-based lookup tables, string manipulation, basic file I/O with `python-docx`.

### Nmap - Zenmap GUI.py (2020)

A GUI automation script for running repeated scans in the Nmap/Zenmap GUI without manually repeating each step by hand. It uses PyAutoGUI to move the mouse and simulate clicks and keystrokes at fixed screen coordinates — entering an IP address, starting a scan, waiting for it to complete, and saving the result — then loops through a list of IP addresses provided by the user.

Because it relies on hardcoded screen coordinates and fixed wait times, it's tied to the specific screen resolution, window layout, and Zenmap version it was built against, and would need coordinates adjusted to work in a different environment.

- Prompts for the Zenmap shortcut location and a list of IP addresses to scan.
- Automates mouse movement, clicks, and keyboard input via PyAutoGUI.
- Main concepts: GUI automation, basic looping/state handling across repeated runs, timing-based coordination with an external application.

### Seperating Frame.py (2020)

A video-processing script that splits a video file into individual frames. It opens the video with OpenCV's `VideoCapture`, reads it frame by frame, resizes each frame to 1280×720, and writes each one out as a sequentially numbered JPEG image.

- Prompts for the input video's filename and path, and a separate path to save the extracted frames.
- Main concepts: reading video with OpenCV, frame-by-frame processing, image resizing, sequential file output.

### vid rec and save.py (2019)

A basic webcam recording script. It opens the default camera device, displays a live preview window, and writes the incoming frames to disk as an AVI file using OpenCV's `VideoWriter`, until the user presses `q` to stop.

The camera device index and the output file path are both hardcoded in the script rather than configurable at runtime, and the output path is a Windows-specific local file location from the original development machine — it would need to be edited directly to run elsewhere.

- Opens camera device `0` and displays a live preview while recording.
- Main concepts: capturing and displaying video frames in real time, writing video to disk with a codec (`XVID`), basic OpenCV setup.

## Technologies Used

- Python
- OpenCV (`cv2`)
- PyAutoGUI
- python-docx

## About These Projects

These are preserved as examples of my earlier programming work from 2019–2021, not as advanced or production-ready applications. They reflect early, self-directed experimentation with automation, computer vision, file processing, and basic text encoding — written while learning Python rather than building toward a specific product. Some scripts depend on Windows-specific file paths, GUI layouts, or software (Nmap/Zenmap) and are not guaranteed to run as-is outside the environment they were originally written for.

    
