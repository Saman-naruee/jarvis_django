# Jarvis Django Assistant 🤖

A Telegram-based AI assistant inspired by Iron Man's JARVIS, built with Django and modern AI capabilities.

## 🌟 Features

- **Multi-AI Provider Support**
  - OpenAI Integration
  - Google Gemini Integration
  - Groq Integration
  - Extensible AI provider system

- **Telegram Integration**
  - Seamless chat interface
  - Real-time responses
  - Multi-user support

- **Advanced Capabilities**
  - Conversation memory
  - Context awareness
  - Personality configuration
  - Action execution system

- **Security & Performance**
  - Rate limiting
  - User authentication
  - Async processing
  - Message queue support

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL
- Telegram Bot Token
- AI Provider API Keys (OpenAI/Gemini/Groq)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Saman-naruee/jarvis_django.git
cd jarvis_django
```

2. **Set up virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
Create a `.env` file:
```env
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=jarvis_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# AI Providers
AI_PROVIDER=openai
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key

# Telegram
TELEGRAM_BOT_TOKEN=your-bot-token
```

5. **Initialize database**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

## 🏗️ Project Structure

```
jarvis_django/
├── ai_providers/          # AI integration modules
│   ├── base.py           # Base AI provider interface
│   ├── openai_provider.py
│   ├── gemini_provider.py
│   └── groq_provider.py
├── assistant/            # Core assistant functionality
├── conversations/        # Conversation management
├── users/               # User management
└── manage.py
```

## 🔧 Configuration

### AI Providers
- Configure different AI providers in `settings.py`
- Switch between providers using environment variables
- Extend `BaseAIProvider` for custom implementations

### Telegram Bot
1. Create a bot with [@BotFather](https://t.me/botfather)
2. Configure webhook for real-time updates
3. Set the bot token in environment variables

## 🛡️ Security

- Rate limiting per user
- API key validation
- Request authentication
- Secure data storage

## 🔄 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgments

- Django Framework
- OpenAI
- Google Gemini
- Groq
- Python Telegram Bot

## 📚 Documentation

Full documentation is available in the `/docs` directory:
- [API Documentation](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Contributing Guidelines](docs/CONTRIBUTING.md)

## 🐛 Bug Reports

Please use GitHub Issues to report any bugs or file feature requests.