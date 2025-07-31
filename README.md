# 🤖 AI Interviewer - Intelligent Interview Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Transform your interview preparation with AI-powered mock interviews that adapt to your resume and job requirements. Practice with personalized questions, voice interaction, and real-time feedback to ace your next interview.**

### 🎯 What is AI Interviewer?

AI Interviewer is an intelligent interview preparation platform that uses advanced AI to create personalized mock interviews. By analyzing your resume and job descriptions, it generates tailored questions that simulate real interview scenarios, helping you practice and improve your interview skills with confidence.

**Key Benefits:**
- 🎯 **Personalized Questions**: AI analyzes your background and target role
- 🗣️ **Voice & Text Interaction**: Practice both verbal and written communication
- 📊 **Real-time Feedback**: Get instant responses and follow-up questions
- 🎭 **Multiple Interview Types**: Behavioral, Technical, and Resume-based
- 🚀 **Easy Setup**: Simple installation with clear documentation

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🚀 Features](#-features)
- [⚙️ Installation](#️-installation)
- [📖 Usage Guide](#-usage-guide)
- [🏗️ Technical Architecture](#️-technical-architecture)
- [🧠 AI & Prompt Design](#-ai--prompt-design)
- [🎥 Demo Video](#-demo-video)
- [🔧 Development](#-development)
- [🤝 Contributing](#-contributing)
- [📞 Contact](#-contact)

## 🎯 Project Overview

**AI Interviewer** is a cutting-edge application that leverages generative AI to conduct personalized mock interviews. Unlike traditional interview preparation tools, this application analyzes your resume and job descriptions to generate tailored questions, providing a realistic interview experience that adapts to your specific background and target role.

### 🎯 Key Capabilities

- **📄 Resume Analysis**: Upload your resume and let AI extract relevant experience
- **🎯 Job-Specific Questions**: Generate questions based on actual job descriptions
- **🗣️ Multi-Modal Interaction**: Choose between text chat or voice interaction
- **🎭 Interview Types**: Behavioral, Technical, and Resume-based interviews
- **🎨 Customizable Experience**: Configure interviewer personality and specialization
- **📊 Real-time Feedback**: Receive instant responses and follow-up questions

## 🚀 Features

### 🎭 Interview Types
- **Behavioral Interviews**: Assess soft skills, leadership, and problem-solving
- **Technical Interviews**: Evaluate technical knowledge and coding abilities
- **Resume-Based Interviews**: Deep dive into your experience and achievements
- **Custom Interviews**: Configure specialized interviewers for specific roles

### 🎨 Interaction Modes
- **💬 Text Chat**: Traditional Q&A format with real-time responses
- **🎤 Voice Interaction**: Natural speech-to-text and text-to-speech
- **📱 Responsive Design**: Works seamlessly on desktop and mobile

## ⚙️ Installation

### Prerequisites

- **Python 3.8+** (3.12 recommended)
- **Git** for cloning the repository
- **OpenAI API Key** for AI functionality
- **AWS Account** (optional, for voice features)

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/SriHarshitha88/Hiring_Assistant_bot.git
cd Hiring_Assistant_bot
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure API Keys

Create `.streamlit/secrets.toml`:
```toml
# Required: OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key_here"

# Optional: AWS Credentials for voice features
aws_access_key_id = "your_aws_access_key_id"
aws_secret_access_key = "your_aws_secret_access_key"
```

#### 5. Run the Application
```bash
streamlit run Homepage.py
```

The application will be available at `http://localhost:8501`

### 🔧 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | ✅ Yes | OpenAI API key for AI functionality |
| `aws_access_key_id` | ❌ No | AWS access key for voice features |
| `aws_secret_access_key` | ❌ No | AWS secret key for voice features |

## 📖 Usage Guide

### 🏠 Getting Started

1. **Launch the Application**
   - Run `streamlit run Homepage.py`
   - Open your browser to `http://localhost:8501`

2. **Choose Interview Type**
   - **Professional**: Technical skills assessment
   - **Behavioral**: Soft skills evaluation
   - **Resume**: Experience-based questions
   - **Customize**: Create personalized interviews

3. **Upload Your Resume** (Optional)
   - Supported formats: PDF, DOCX, TXT
   - AI will extract relevant experience and skills

4. **Provide Job Description** (Optional)
   - Paste the job posting or description
   - AI will tailor questions to match requirements

5. **Select Interaction Mode**
   - **Chat**: Text-based interaction
   - **Voice**: Speech-to-text and text-to-speech

6. **Start Your Interview**
   - Introduce yourself
   - Answer AI-generated questions
   - Receive real-time feedback

### 🎯 Interview Flow

```
Upload Resume → Provide Job Description → Choose Interview Type → 
Select Interaction Mode → Start Interview → Answer Questions → 
Receive Feedback → Continue or End Session
```

### 💡 Pro Tips

- **Be Specific**: Provide detailed job descriptions for better question targeting
- **Use Voice Mode**: Practice verbal communication skills
- **Review Responses**: Analyze your answers to identify improvement areas
- **Multiple Sessions**: Practice different interview types for comprehensive preparation

## 🏗️ Technical Architecture

### 🏛️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   AI Services   │
│   (Streamlit)   │◄──►│   (Python)      │◄──►│   (OpenAI)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Voice I/O     │    │   Vector Store  │    │   AWS Polly     │
│   (Speech)      │    │   (FAISS)       │    │   (TTS)         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 📚 Technology Stack

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Frontend** | Streamlit | 1.25.0 | Web interface and UI |
| **AI Framework** | LangChain | 0.3.27 | LLM orchestration |
| **Language Model** | OpenAI GPT-4 | Latest | Question generation |
| **Vector Database** | FAISS | 1.11.0 | Semantic search |
| **Voice Synthesis** | AWS Polly | Latest | Text-to-speech |
| **Speech Recognition** | OpenAI Whisper | Latest | Speech-to-text |
| **Document Processing** | PyPDF2 | 3.0.1 | Resume parsing |
| **Audio Recording** | Custom Component | 0.0.10 | Voice input |

### 🏗️ Project Structure

```
ai-interviewer/
├── 📁 Main Application
│   ├── Homepage.py              # Main entry point
│   ├── app_utils.py             # Navigation utilities
│   └── initialization.py        # App initialization
│
├── 📁 Interview Screens
│   ├── Behavioral Screen.py     # Soft skills assessment
│   ├── Professional Screen.py   # Technical assessment
│   └── Resume Screen.py        # Experience-based
│
├── 📁 AI & ML
│   ├── prompts/                 # Interview prompts
│   └── speech_recognition/      # Voice processing
│
├── 📁 Voice Features
│   ├── aws/                     # AWS Polly integration
│   └── st_audiorec/            # Audio recording
│
├── 📁 Configuration
│   └── .streamlit/             # App config & secrets
│
└── 📁 Static Assets
    ├── static/                  # CSS & images
    └── images/                  # App assets
```

### 🔄 Conversation Flow Management

```
Initial Greeting → Resume Analysis → Question Generation → 
Response Analysis → Follow-up Questions → Feedback → 
Next Question → Session Summary
```

### 📊 Response Analysis

The AI analyzes responses for:
- **Technical Accuracy**: Factual correctness
- **Communication Skills**: Clarity and structure
- **Cultural Fit**: Alignment with company values
- **Leadership Potential**: Decision-making and initiative

## 🎥 Demo Video

> **📹 Watch AI Interviewer in Action**

[![AI Interviewer Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

*Click the image above to watch a comprehensive demo of AI Interviewer features*

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### 🚀 Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with proper documentation
4. Add tests for new functionality
5. Submit a pull request

### 📋 Contribution Guidelines
- **Code Style**: Follow PEP 8 standards
- **Documentation**: Add docstrings for new functions
- **Testing**: Include unit tests for new features
- **Commits**: Use conventional commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing the GPT-4 API
- **Streamlit** for the amazing web framework
- **LangChain** for LLM orchestration
- **FAISS** for vector similarity search
- **AWS** for text-to-speech capabilities

---

<div align="center">

</div>