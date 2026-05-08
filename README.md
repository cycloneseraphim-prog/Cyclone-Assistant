# Cyclone Assistant

A ChatGPT-like AI chatbot built with Python and OpenAI API.

## Features

- Conversational AI powered by OpenAI GPT models
- Chat history management
- Easy-to-use command-line interface
- Customizable system prompts
- Token usage tracking

## Requirements

- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cycloneseraphim-prog/Cyclone-Assistant.git
cd Cyclone-Assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows: set OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the chatbot:
```bash
python main.py
```

Start chatting! Type `exit` or `quit` to end the conversation.

## Project Structure

```
Cyclone-Assistant/
├── main.py                 # Main chatbot application
├── config.py              # Configuration settings
├── chatbot.py             # Chatbot core logic
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## License

MIT License
