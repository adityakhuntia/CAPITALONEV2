# CAPITALONEV2

CAPITALONEV2 is a versatile AI-driven project developed by Aditya Khuntia and Anik Dey from Delhi Technological University. It integrates Automatic Speech Recognition (ASR), WhatsApp messaging, Retrieval-Augmented Generation (RAG), and external APIs like WeatherBit and ENAM for a comprehensive conversational AI experience.

## 🚀 Features

- **Automatic Speech Recognition (ASR)**: Supports both offline and cloud-based speech-to-text processing.
- **WhatsApp Integration**: Enables interaction via WhatsApp using a Flask-based server.
- **ENAM Agent**: Provides agricultural market insights.
- **WeatherBit Agent**: Delivers weather-related data.
- **RAG Integration**: Enhances responses with context-aware, knowledge-grounded information.
- **Translation and Intent Classification**: Supports multilingual interactions and intent detection.
- **Task Scheduling**: Manages automated tasks and workflows.

## 📂 Repository Structure

```
├── audio_flow.py               # Offline audio processing pipeline
├── faster_whisper_stt.py       # Whisper-based speech recognition
├── whisper_stt.py              # Whisper-based speech recognition
├── whisper.cpp                 # Whisper C++ implementation
├── sarvam_stt_cloud.py         # Cloud-based speech-to-text
├── sarvam_cloud.py             # Cloud-based speech processing
├── intent_classify.py          # Intent classification logic
├── enam.py                     # ENAM agent for agricultural data
├── sarvam_translate.py         # Translation module
├── sarvam_translate2.py        # Additional translation module
├── FlaskWhatsAppServer/        # Flask endpoint for WhatsApp integration
├── whatsapp.py                 # WhatsApp flow logic
├── RAG.py                      # Retrieval-Augmented Generation pipeline
├── scheduler.py                # Task scheduling
├── weatherbit.py               # WeatherBit API integration
├── temp.py                     # Miscellaneous/testing scripts
├── audio.mp3                   # Sample audio file
├── bfg.jar                     # Auxiliary utility
├── docs/                       # Optional documentation
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🔧 Prerequisites

- **Python**: 3.8 or higher
- **Optional**: `whisper.cpp` for offline audio processing
- **Cloud Services**: Access to cloud-based STT services (e.g., Sarvam) for online mode
- **Internet**: Required for RAG, WhatsApp, and external API integrations

## 🔑 Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/adityakhuntia/CAPITALONEV2.git
   cd CAPITALONEV2
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 🚀 Running the Project

Run the scheduler to start the application:

```bash
python scheduler.py
```

## 🔧 Configuration

- Create a `.env` file in the project root to store sensitive information (e.g., API keys for WeatherBit, Sarvam, or WhatsApp):

  ```env
  WEATHERBIT_API_KEY=your_weatherbit_api_key
  SARVAM_API_KEY=your_sarvam_api_key
  WHATSAPP_TOKEN=your_whatsapp_token
  ```
- Ensure the necessary API credentials are configured for RAG, WeatherBit, and WhatsApp integrations.

## 📚 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For questions or feedback, please contact adityakhuntia or notanikdey.
