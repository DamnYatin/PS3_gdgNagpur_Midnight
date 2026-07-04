<!-- cat << 'EOF' > README.md -->
# AI-Powered Agriculture Platform
## Hackathon Architecture & Deployment Plan/

---

## Vision

Build an AI-powered agricultural assistant that helps farmers make better farming decisions using text, voice, and image recognition while remaining accessible even to farmers who do not own smartphones.

---

## Problem Statement

India has over **263 million people engaged in agriculture**, but many farmers still face significant challenges:

* Limited access to agricultural experts
* Lack of timely crop disease diagnosis
* Language barriers
* Low digital literacy

Our goal is to provide instant, affordable, and localized agricultural guidance powered entirely by AI and accessible through multiple channels.

---

## Target Users

### Primary Users
* Farmers with smartphones

### Secondary Users
* Farmers using feature phones
* Elderly farmers
* Farmers with low literacy
* Farmers in remote villages

---

## Accessibility Models (Future Implementations)

### 1. Web App
* Voice input capabilities
* Image upload for disease detection
* AI chatbot interface
* Government schemes & crop advisory dashboards

### 2. Voice Call (IVR)
* Farmer speaks into a toll-free number
* Speech-to-Text translation
* AI processes request
* Text-to-Speech conversion
* Voice response returned (No smartphone required)

### 3. Missed Call Service
* Farmer gives a missed call
* System automatically calls back
* AI interacts through voice

### 4. SMS Support
* Send text: **CROP WHEAT**
* Receive text: **Rain expected tomorrow. Avoid irrigation today.**
* Works seamlessly on feature phones

### 5. Village Digital Kiosks
* Deployed at Common Service Centres (CSC), Panchayat Offices, Krishi Vigyan Kendras (KVKs), and Farmer Producer Organizations (FPOs)
* Operators assist farmers using the AI platform desktop view

### 6. Agri Shops
* Seed and fertilizer shops upload crop photos on behalf of farmers
* Detect diseases and recommend targeted pesticides
* Print recommendations instantly

### 7. Agriculture Extension Officers
* Field officers visit farms and capture images
* Record observations and receive AI recommendations
* Explain AI-generated insights directly to farmers

---

## Core Features

### AI Chat Assistant
* Supports Hindi, Marathi, English, and other regional languages
* Answers questions about crop care, fertilizers, government schemes, irrigation, and pest control

### Voice Recognition
* Farmer speaks naturally (e.g., "My tomato leaves are turning yellow")
* AI understands context and responds with actionable advice

### Image Recognition
* Farmer uploads crop image
* AI detects diseases, nutrient deficiencies, or pest attacks
* Returns a confidence score, possible causes, and recommended actions


### Market Price Information
* Provides nearby mandi prices, historical trends, and suggestions on when to sell

---

## Technology Stack

### Frontend & UI
* Core: HTML5, Vanilla JavaScript, and Vanilla CSS. (No heavy frameworks like React or Tailwind are used, keeping it lightweight and fast)
* Styling: CSS3 Custom Properties (variables), CSS Grid for the layout, and keyframe animations for the pulsating buttons
* **Vercel:** For frontend deployment


### Backend & Core Logic
* **Python 3.10+:** Core runtime
* **Web Framework:** Flask (a lightweight WSGI web application framework)
* **Security/Middleware:** Flask-CORS to allow your Vercel frontend to make cross-origin requests to your PythonAnywhere backend
* **Hosting / Deployment:** PythonAnywhere (using WSGI to serve the Python app).

### AI Components
* **Speech-to-Text:** Whisper API (OpenAI)
* **Text-to-Speech:** Google TTS (gTTS) or ElevenLabs API

### Database & Storage
* **Database:** SQLite3 (via the mandi_compare.db file) for storing crops, mandis, and pricing data.

---

## Installation & Local Setup

Follow these steps to run the Streamlit application on your local machine.

### Prerequisites
* Python 3.10 or higher installed
* Git installed

### Step-by-Step Guide

**1. Clone the repository**
Open your terminal and clone the repository:
```
git clone https://github.com/yourusername/agri-ai-platform.git
```
```
cd agri-ai-platform
```

**2. Install dependencies**
Install all required Python packages using pip:
```
pip install -r requirements.txt
```

**3. Access the App**
Open your web browser and navigate to `http://localhost:8501`

