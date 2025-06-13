# AI Toolkit
#### Author: Bocaletto Luca

Zero-registration, local AI toolkit for offline text summarization, question-answering, audio transcription, and image captioning on Debian/Ubuntu derivatives.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🔍 Features

- Text summarization via HuggingFace T5  
- Question-answering with DistilBERT-SQuAD  
- Audio transcription using OpenAI Whisper (local)  
- Image captioning with Salesforce BLIP  

## 📁 Repository Layout

```
ai_toolkit/
├── requirements.txt      # Python dependencies
├── app.py                # CLI entrypoint
└── tasks/
    ├── summarizer.py     # summarize(text)
    ├── qa.py             # answer(question, context)
    ├── transcription.py  # transcribe(audio_path)
    └── image_caption.py  # caption_image(image_path)
```

## 🚀 Installation

```bash
sudo apt update
sudo apt install -y python3-venv ffmpeg git
git clone https://github.com/youruser/ai_toolkit.git
cd ai_toolkit
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 🛠️ Usage

```bash
# Summarize a text file:
python app.py summarize path/to/article.txt

# Question-Answering on a document:
python app.py qa "What is the main topic?" path/to/article.txt

# Transcribe an audio file:
python app.py transcribe path/to/audio.mp3

# Generate a caption for an image:
python app.py caption path/to/photo.jpg
```

Each command will print the result to stdout.

## 💡 Extending

- Wrap with Flask or FastAPI for a web UI  
- Deploy models on GPUs by installing `torch` with CUDA support  
- Schedule tasks via `cron` or systemd timers  

## 🤝 Contributing

1. Fork the repo  
2. Create a branch (`git checkout -b feat/awesome`)  
3. Commit changes (`git commit -m "feat: add X"`)  
4. Push (`git push origin feat/awesome`)  
5. Open a Pull Request  

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

#### This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  
