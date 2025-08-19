# CAPITALONEV2

CAPITALONEV2 is a versatile AI-driven project developed by Aditya Khuntia & Anik Dey (Delhi Technological University) featuring:

- **ASR (Automatic Speech Recognition) Flow**
- **WhatsApp Integration Flow**
- **ENAM Agent**
- **WeatherBit Agent**
- Integrated with RAG (Retrieval-Augmented Generation)
- Local and cloud-based speech processing options

---

##  Project Contents

The repository includes the following components:

- **ASR and Audio Processing**
  - `audio_flow.py` – Offline audio processing pipeline
  - `faster_whisper_stt.py`, `whisper_stt.py`, `whisper.cpp` – Whisper-based speech recognition
  - `sarvam_stt_cloud.py`, `sarvam_cloud.py` – Cloud-based speech-to-text options

- **Intent & Translation Agents**
  - `intent_classify.py`
  - `enam.py`
  - `sarvam_translate.py`, `sarvam_translate2.py`

- **WhatsApp Flow**
  - `FlaskWhatsAppServer` (Flask endpoint)
  - `whatsapp.py`

- **RAG Integration**
  - `RAG.py`

- **Others**
  - `scheduler.py` – Task scheduling
  - `weatherbit.py` – WeatherBit integration
  - `temp.py` – Miscellaneous/testing scripts
  - `audio.mp3`, `bfg.jar` – Auxiliary files and utilities
  - `docs/` – Optional documentation

---

##  Prerequisites

- Python **3.8+**
- Optional: **whisper.cpp** (for offline audio processing)
- Access to cloud STT services (for online mode)
- Internet access for RAG and WhatsApp flows

---

##  Setup & Installation

Clone the repository and enter its directory:
```bash
git clone https://github.com/adityakhuntia/CAPITALONEV2.git
cd CAPITALONEV2

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate    # Linux/macOS
# or
.\venv\Scripts\activate     # Windows

Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt


## Running the Project:
Just run scheduler.py 
